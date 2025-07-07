# image_generator.py
from gradio_client import Client, handle_file

client = Client("multimodalart/Ip-Adapter-FaceID")

def generate_image(image_url: str, prompt: str, negative_prompt: str = "", face_strength: float = 1.3, likeness_strength: float = 1.0):
    print("Generating image with:")
    print("🖼️ Image URL:", image_url)
    print("✨ Prompt:", prompt)
    print("🚫 Negative Prompt:", negative_prompt)

    try:
        result = client.predict(
            images=[handle_file(image_url)],
            prompt=prompt,
            negative_prompt=negative_prompt,
            preserve_face_structure=True,
            face_strength=face_strength,
            likeness_strength=likeness_strength,
            nfaa_negative_prompt="naked, bikini, skimpy, scanty, bare skin, lingerie, swimsuit, exposed, see-through",
            api_name="/generate_image"
        )
        print("✅ Result:", result)
        return result
    except Exception as e:
        print("❌ Gradio Inference Error:", str(e))
        raise e
