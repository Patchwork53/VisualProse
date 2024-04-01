

def image_gen_call(pipe, base_prompt):
    positive_prompt = "high quality, 4K HDR"
    negative_prompt = "nsfw, bad quality, bad anatomy, worst quality, low quality, low resolutions, extra fingers, blur, blurry, ugly, wrongs proportions, watermark, image artifacts, lowres, ugly, jpeg artifacts, deformed, noisy image"

    prompt = base_prompt+", "+positive_prompt

    image = pipe(
        prompt,
        negative_prompt=negative_prompt,
        width=1024,
        height=1024,
        guidance_scale=4,
        num_inference_steps=20
    ).images[0]

    return image