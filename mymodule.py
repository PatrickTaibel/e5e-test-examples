import numpy as np
import pandas as pd
from PIL import Image
from weasyprint import HTML


def myfunction(event, context):
    print("================ WeasyPrint ================")
    HTML('http://weasyprint.org/').write_pdf('/tmp/weasyprint-website.pdf')
    print("Done!")
    print()

    print("================ Pillow ================")
    img = Image.new(mode='RGB', size=(100, 100), color=(50, 50, 50))
    img.save("/tmp/pillow.jpeg")
    img.save("/tmp/pillow.png")
    print("Done!")
    print()

    print("================ Numpy ================")
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a)
    print("Done!")
    print()

    print("================ Pandas ================")
    df = pd.DataFrame(
        {
            "Name": [
                "Test1",
                "Test2",
                "Test3"
            ],
            "Age": [1, 2, 3]
        }
    )
    print(df)
    print("Done!")
    print()


if __name__ == "__main__":
    myfunction({}, {})
