from abc import ABC, abstractmethod
from typing import List

from common.request import Sequence, Request


class TokenCounter(ABC):
    @abstractmethod
    def count_tokens(self, request: Request, completions: List[Sequence]) -> int:
        """
        Counts the total number of tokens given a request and completions.
        """
        pass

    @abstractmethod
    def estimate_tokens(self, request: Request) -> int:
        """
        Given a request, roughly estimate the number of tokens.
        """
        pass

    @abstractmethod
    def tokenize_and_count(self, model: str, text: str) -> int:
        """
        Tokenizes the text and counts the number of tokens.
        """
        pass

    @abstractmethod
    def fits_within_context_window(self, model: str, text: str, expected_completion_token_length: int) -> bool:
        """
        Whether the given text fits within the context window given the model and
        expected token length of the completion.
        """
        pass

    @abstractmethod
    def truncate_from_right(self, model: str, text: str) -> str:
        """
        Truncates text from the right to fit within the given model's context window.
        """
        pass