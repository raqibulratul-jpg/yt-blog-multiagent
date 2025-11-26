from typing import List


def chunk_text(text: str, max_chars: int = 1000) -> List[str]:
    """
    Naive text chunker that splits on paragraphs and respects a max character budget.
    """
    if not text:
        return []

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks: List[str] = []
    current = ""

    for para in paragraphs:
        if not current:
            current = para
        elif len(current) + len(para) + 1 <= max_chars:
            current = current + "\n" + para
        else:
            chunks.append(current)
            current = para

    if current:
        chunks.append(current)

    return chunks


def compact_context(chunks: List[str], max_chunks: int = 3) -> str:
    """
    Simple context compaction: keep first N chunks.
    """
    return "\n\n".join(chunks[:max_chunks])
