from unstructured.partition.text import partition_text

elements = partition_text("../../data/黑神话悟空/设定.txt")

for i, element in enumerate(elements):
    print(f"\n--- Element {i+1} ---")
    print(f"元素类型: {element.__class__.__name__}")
    print(f"元素内容: {element.text}")
    if hasattr(element, "metadata"):
        print("元数据: ")
        metadata = vars(element.metadata)
        valid_metadata = {k: v for k, v in metadata.items() if not k.startswith("_") and v is not None}
        for k, v in valid_metadata.items():
            print(f"{k}: {v}")
