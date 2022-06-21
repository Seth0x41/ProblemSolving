class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        tmp=[]
        word=[]
        products.sort()
        for char in searchWord:
            word.append(char)
            text = "".join(word)
            for product in products:
                if product.startswith(text):
                    tmp.append(product)
                else:
                    continue
            if len(tmp) > 3:
                result.append(tmp[:3])
                tmp.clear()
            else:
                result.append(tmp[:])
                tmp.clear()
        return result
