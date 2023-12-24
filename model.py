from langchain.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = """
Вопрос: {question}

Ответ: Давайте подумаем над этим шаг за шагом."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = LlamaCpp(model_path="saiga_mistral_7b.Q4_K_M.gguf",  # Download the model file first
               n_ctx=32768,      # The max sequence length to use - note that longer sequence lengths require much
                                 # more resources
               n_threads=8,      # The number of CPU threads to use, tailor to your system and the resulting performance
               n_gpu_layers=35,  # The number of layers to offload to GPU, if you have GPU acceleration available
               max_tokens=2000
               )
llm_chain = LLMChain(prompt=prompt, llm=llm)


def generate(text):
    try:
        output = llm_chain.run(text)
        return output
    except Exception as e:
        return e
