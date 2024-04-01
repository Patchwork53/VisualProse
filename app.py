
from flask import Flask, render_template, request, jsonify
import torch
from diffusers import (
    StableDiffusionXLPipeline,
    KDPM2AncestralDiscreteScheduler,
    AutoencoderKL
)

import google.generativeai as genai
from scripts.llm_call import gemini_call
from scripts.image_gen_call import image_gen_call
from scripts.log import log
from scripts.save_image import save_image
from resources.prompt_templates import core_message_extraction_instruction_key, abstract_depiction_instruction_key, summary_extraction_instruction_key


app = Flask(__name__)

vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix",
    torch_dtype=torch.float16,
    cache_dir="D:/hf_cache/"
)

pipe = StableDiffusionXLPipeline.from_pretrained(
    "dataautogpt3/ProteusV0.4",
    vae=vae,
    torch_dtype=torch.float16,
    cache_dir="D:/hf_cache/"
)
pipe.scheduler = KDPM2AncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

print("MODEL LOADED")

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel(
    "gemini-pro",
    safety_settings=[
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        article = request.form['article']
        summary = gemini_call(model, summary_extraction_instruction_key, article)
        core_message = gemini_call(model, core_message_extraction_instruction_key, article)
        abstract_depiction = gemini_call(model, abstract_depiction_instruction_key, summary+" "+core_message)
        return jsonify({'core_message': summary+" "+core_message, 'abstract_depiction': abstract_depiction})
    return render_template('index.html')



    
@app.route('/generate', methods=['POST'])
def generate():


    base_prompt = request.form['prompt']

    article = request.form['article']
    core_message = request.form['core_message']
    prompt = request.form['prompt']

    log(article, core_message, prompt)

    image = image_gen_call(pipe, base_prompt)

    image_name = save_image(image)

    return jsonify({'image_name': f"{image_name}"})

if __name__ == '__main__':
    app.run(debug=True)
