# Slide Generator

Use LLM generate Marp slides

This is a retrieval augmented generation application.

We can have a pre-defined slide outlines.

For each outlines, we will have prompt to guide for generation. (we will have a page that can configure this)

In addition, we can have agents that download related figure or extract figure from the document.

1. For each document we will use LlamaIndex for vector storage.
2. Prompts for each page, for example "What is the motivation of this document, summarize into 3 bullet points."
3. We will use Marp to generate slides and can easily convert to different slides format.

## Todo

- [ ] Most basic "Upload document -> LlamaIndex -> LLM -> Marp" pipeline
- [ ] Customized LLM prompt config page (or config file)
- [ ] CLI tool
- [ ] Online demo
- [ ] Multi-modal
  - [ ] Able to add image from document
  - [ ] Able to add image from the web
  - [ ] Able to capture table from document
    - [Multi-Modal on PDF’s with tables. - LlamaIndex 🦙 0.9.22](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pdf_tables.html)

## Resources

- LLM - [LangChain](https://www.langchain.com/)
- Vector Store - [LlamaIndex - Data Framework for LLM Applications](https://www.llamaindex.ai/)
  - [run-llama/llama_index: LlamaIndex (formerly GPT Index) is a data framework for your LLM applications](https://github.com/run-llama/llama_index)
  - [Azure OpenAI - LlamaIndex 🦙 0.9.22](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI.html)
- Slide Generation - [Marp: Markdown Presentation Ecosystem](https://marp.app/)
