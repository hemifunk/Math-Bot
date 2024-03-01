from utils import create_keyboard

TOKEN = "6835045984:AAFs2I3CG7xxHEeTkVNsfjYFRy1PnYgsVGg"

TOPICS = [
    "בעיות תנועה", "פונקציית מנה", "פונקציית שורש",
    "פונקציית טריגו", "הסתברות", "סדרות", 
    "בעיות תנועה", "טריגונומטריה", "גיאומטריה"
]

TOPICS_REGEX_PATTERN = "|".join(TOPICS)

TOPIC_OPTIONS = [
    "שיעורים מוקלטים", "הצטרפות לקהילה", "תוכנית למידה", "בחינות עבר"
]

START_MENU_KEYBOARD = create_keyboard(TOPICS)

TOPIC_OPTIONS_KEYBOARD = create_keyboard(TOPIC_OPTIONS)