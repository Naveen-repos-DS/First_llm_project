from transformers import pipeline


generator = pipeline('text-generation', model='distilgpt2')

result = generator(
    "AI is the future because",
    max_length = 50, # 50 tokens is the maximum length of the generated text
    num_return_sequences = 1 # 1 different sequence will be generated
)


print(result[0]['generated_text'])