from unstructured.partition.auto import partition

elements = partition(
    filename="../../data/黑神话悟空/黑神话悟空.pdf",
    content_type="application/pdf"
)

for element in elements:
    print(element)