import argparse
from pathlib import Path
from tqdm import tqdm

# torch

import torch

from einops import repeat

# vision imports

from PIL import Image
from torchvision.utils import make_grid, save_image

# dalle related classes and utils

from dalle_pytorch import OpenAIDiscreteVAE,  DALLE
from dalle_pytorch.tokenizer import tokenizer


# generate images
inputs="hi five"  # String to generate image
num_images=1
batch_size = 1
texts = inputs.split('|')
top_k=0.9



def exists(val):
    return val is not None

# tokenizer

# load DALL-E

dalle_path = Path("dalle.pt")

assert dalle_path.exists(), 'trained DALL-E must exist'

load_obj = torch.load(str(dalle_path))
dalle_params, vae_params, weights = load_obj.pop('hparams'), load_obj.pop('vae_params'), load_obj.pop('weights')

dalle_params.pop('vae', None) # cleanup later

vae = OpenAIDiscreteVAE()


dalle = DALLE(vae = vae, **dalle_params).cuda()

dalle.load_state_dict(weights)
image_size = vae.image_size


for text in tqdm(texts):
    text = tokenizer.tokenize([inputs], dalle.text_seq_len).cuda()

    text = repeat(text, '() n -> b n', b = num_images)

    outputs = []

    for text_chunk in tqdm(text.split(batch_size), desc = f'generating images for - {text}'):
        output = dalle.generate_images(text_chunk, filter_thres = top_k)
        outputs.append(output)

    outputs = torch.cat(outputs)

    # save all images
    # This should be sent from server to client
    outputs_dir = Path("./outputs") / inputs.replace(' ', '_')[:(100)]
    outputs_dir.mkdir(parents = True, exist_ok = True)

    for i, image in tqdm(enumerate(outputs), desc = 'saving images'):
        save_image(image, outputs_dir / f'{i}.jpg', normalize=True)

    print(f'created {num_images} images at "{str(outputs_dir)}"')