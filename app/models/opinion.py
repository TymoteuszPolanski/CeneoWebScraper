from app.parameters import selectors
from app.utils import get_item

class Opinion():
    def __init__(self, author="", recommendation=None, stars=0, content="", useful=0, useless=0, published=None, purchased=None, pros=[], cons=[], opinion_id=""):
        self.author=author
        self.recommendation=recommendation
        self.stars=stars
        self.content=content
        self.useful=useful
        self.useless=useless
        self.published=published
        self.purchased=purchased
        self.pros=pros
        self.cons=cons
        self.opinion_id=opinion_id
        return self

    def extract_opinion(self, opinion):
        for key, value in selectors.items():

            setattr(self, key, get_item(opinion, *value))
                    
        self.single_opinion["opinion_id"] = opinion["data-entry-id"]
        return self

    def __str__(self) -> str:     
        pass

    def __repr__(self) -> str:
        pass

    def to_dict(self) -> dict:
        pass