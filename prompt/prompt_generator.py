from langchain_core.prompts import PromptTemplate

#template
template= PromptTemplate(

    template= """please summarise the research paper titled {paper_input} in a {style_input} style and in {length_input} length""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')