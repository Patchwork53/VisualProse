# Visual Prose
Turn entire articles into art
<br>
<img src="https://github.com/Patchwork53/VisualProse/blob/main/resources/image.png?raw=true" width=650>

## Technical Description
The users inputs a long passage, article or blog post. An LLM is called to summarize the document. It's called again to extract the *core message* of the document. The summary and the core message are combined and sent as input to the LLM a third time to generate an artistic depiction. This time, the LLM is rigorously instruction-scaffolded and supplied with few-shot examples of how to best represent articles as images. Exact prompt structures are in the `resourses` folder. The user is allowed to modify the artistic description or try again. Finally, the artistic description is fed to an image generation model. The image generation model adds a set class of positive and negative prompts to enhance quality. The image generation call script is inside the `scripts` folder.

The LLM and Image Generation models can be swapped out. We use the free tier of Gemini and Proteus0.4, however any model combination will work with minor changes to `scripts`.

## Requirements
- Nvidia RTX3060 12GB or higher
- 15GB of storage

## Installation
- Install CUDA and CUDnn for Nvidia GPU
- Install flask
- Install PyTorch
- Install the following python packages.
```
pip install diffusers invisible_watermark transformers accelerate safetensors
```
## Free Gemini API Key
https://ai.google.dev/tutorials/setup

## Proteus0.4
https://huggingface.co/dataautogpt3/ProteusV0.4

## Examples
Article: https://timdettmers.com/2022/03/13/how-to-choose-your-grad-school/
Abstract Depiction:
<img src="https://github.com/Patchwork53/VisualProse/blob/main/resources/dettmers_grad.png?raw=true" width=400>
<br>
Article: https://timdettmers.com/2019/09/03/creativity-in-academia/
Abstract Depiction:
<img src="https://github.com/Patchwork53/VisualProse/blob/main/resources/dettmers_creativity.png?raw=true" width=400>
<br>
Article: https://www.thedailystar.net/supplements/independence-day-special-2015/the-fabric-identity-73752
Abstract Depiction:
<img src="https://github.com/Patchwork53/VisualProse/blob/main/resources/bengal.png?raw=true" width=400>
