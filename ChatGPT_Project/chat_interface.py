
import openai

class interface:
    def __init__(self):
        self.__question = ""
        self.__response = ""

    def answer_question(self, question):
        self.__question = question

        # Set up your API key
        openai.api_key = "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"

        # Set up the parameters for your request
        prompt = question
        model = "text-davinci-002"
        temperature = 0.5
        max_tokens = 100

        # Send the request to the OpenAI API and get the response
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        # Sets and returns the generated response
        self.__response = response.choices[0].text
        return self.__response
