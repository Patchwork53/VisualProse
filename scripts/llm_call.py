import ast
import json

def gemini_call(model, instruction_key, base_text):

    instruction, json_key = instruction_key
    prompt = f"{instruction}\n\n{base_text}"

    response = model.generate_content(prompt)
    try:
        response = response.text.strip()
    except Exception as e:
        print("api call error")
        response = response.parts[0].text.strip()

    # Load the response as a JSON object
    response = response.replace("json","").replace("```","").strip()
    print(response)


    try:
        response = json.loads(response)
    except Exception as e:
        try:
            response = ast.literal_eval(response)
        except Exception as e:
            print("json load error")
            return gemini_call(model, instruction_key, base_text)
    
    print("json loaded")
    if json_key in response:
        return response[json_key]
    else:
        print("json key error")
        return gemini_call(model, instruction_key, base_text)
