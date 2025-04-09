# 🧠 Пример парсинга команды (agent/command_parser.py):

def parse_user_input(text: str) -> dict:
    """
    Преобразует текст команды в структуру:
    {
        'action': 'rename_files',
        'params': { 'folder': 'data/', 'ext': 'pdf' }
    }
    """
    # (Здесь может быть использование LLM или регулярки)
    if "переименуй" in text and "pdf" in text:
        return { 'action': 'rename_files', 'params': { 'folder': 'data/', 'ext': 'pdf' } }
    return { 'action': 'unknown', 'params': {} }