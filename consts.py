from utils import create_keyboard

TOKEN = "6835045984:AAFs2I3CG7xxHEeTkVNsfjYFRy1PnYgsVGg"

TOPICS = [
    "בעיות מילוליות", "פונקציית מנה", "פונקציית שורש",
    "פונקציית טריגו", "הסתברות", "סדרות", 
    "אינטגרלים", "טריגונומטריה", "גיאומטריה"
]

TOPICS_REGEX_PATTERN = "|".join(TOPICS)

TOPIC_OPTIONS = [
    "שיעורים מוקלטים", "הצטרפות לקהילה", "תוכנית למידה", "בחינות עבר"
]

START_MENU_KEYBOARD = create_keyboard(TOPICS)

TOPIC_OPTIONS_KEYBOARD = create_keyboard(TOPIC_OPTIONS)

CHOOSE_OPTION = 0

WORD_PROBLEMS_LESSONS = """*שיעור 1 – בעיות תנועה:*\n https://vimeo.com/499326796?share=copy\n
*שיעור 2 – בעיות הספק ועבודה:*\nhttps://vimeo.com/499326796?share=copy\n
*שיעור 3 – בעיות מילוליות עם אי שוויונות:*\n https://vimeo.com/499326796?share=copy\n
*שיעור 4 – בעיות מילוליות עם פרמטרים:*\n https://vimeo.com/499326796?share=copy\n
*שיעור 5 – בעיות מילוליות עם בעיות קיצון:*\n https://vimeo.com/499326796?share=copy
"""

SERIES_LESSONS = """*שיעור 1 – סדרה חשבונית הגדרה ותכונות:*\n https://vimeo.com/499728559?share=\n
*שיעור 2 – סכום סדרה חשבונית:*\n https://vimeo.com/499731179?share=copy\n
*שיעור 3 – סדרה הנדסית הגדרה ותכונות:*\n https://vimeo.com/499732707?share=copy\n
*שיעור 4 – סדרה הנדסית מיומנות אלגברית:*\n https://vimeo.com/499735152?share=copy\n
*שיעור 5 – סכום סדרה הנדסית:*\n https://vimeo.com/499750077?share=copy\n
*שיעור 6 – סדרה הנדסית אינסופית:*\n https://vimeo.com/499751280?share=copy
"""

ROOT_FUNCTIONS_LESSONS = """*שיעור 1 – תחום הגדרה של פונקציית שורש:*\n https://vimeo.com/496686257?share=copy\n
*שיעור 2 – נגזרת, משיק ונק' קיצון של פונ' שורש:*\n https://vimeo.com/498746632?share=copy\n
*שיעור 3 – אסימפטוטות של פונ' שורש:*\n https://vimeo.com/496848243?share=copy\n
*שיעור 4 – חקירת פונקציית שורש:*\n https://vimeo.com/496849546?share=copy\n"""

GEOMETRY_LESSONS = """*שיעור 1 – סוגי משולשים וחפיפת משולשים:*\n https://vimeo.com/502554488?share=copy\n
*שיעור 2 – משולש ישר זווית:*\n https://vimeo.com/502568803?share=copy\n
*שיעור 3 – משפחת המרובעים:*\n https://vimeo.com/502702270?share=copy\n
*שיעור 4 – קטע אמצעים ונק' מפגש התיכונים:*\n https://vimeo.com/502716034?share=copy\n
*שיעור 5 – דמיון משולשים:*\n https://vimeo.com/502787901?share=copy\n
*שיעור 6 – משפט תאלס ומשפט חוצה זווית:*\n https://vimeo.com/502749393?share=copy\n
*שיעור 7 – זוויות, מיתרים וקשתות במעגל:*\n https://vimeo.com/503125135?share=copy\n
*שיעור 8 – המשיק למעגל:*\n https://vimeo.com/503169197?share=copy\n
*שיעור 9 – מעגל חוסם ומעגל חסום:*\n https://vimeo.com/503202833?share=copy\n
*שיעור 10 – פרופורציות במעגל:*\n https://vimeo.com/503494778?share=copy\n
"""


TRIGONOMETRY_FUNCTIONS_LESSONS = """*שיעור 1 – משוואות טריגונומטריות כלליות:*\n https://vimeo.com/496852858?share=copy\n
*שיעור 2 – משוואות טריגונומטריות מיוחדות:*\n https://vimeo.com/496924693?share=copy\n
*שיעור 3 – פונ' טריגונומטריות זוגיות ואי זוגיות:*\n https://vimeo.com/497583098?share=copy\n
*שיעור 4 – נגזרת ומשיק של פונקציית טריגו:*\n https://vimeo.com/496925542?share=copy\n
*שיעור 5 – נק' קיצון של פונקציית טריגו:*\n https://vimeo.com/496926657?share=copy\n
*שיעור 6 – אסימפטוטות של פונ' טריגו:*\n https://vimeo.com/496927838?share=copy\n
*שיעור 7 – חקירת פונקציית טריגו:*\n https://vimeo.com/497580843?share=copy\n"""


PROPABILITY_LESSONS = """*שיעור 1 – מושגים בסיסיים בהסתברות:*\n https://vimeo.com/500360222?share=copy\n
*שיעור 2 – פתרון שאלון עם דיאגרמת עץ:*\n https://vimeo.com/500371750?share=copy\n
*שיעור 3 – התפלגות בינומית ונוסחת ברנולי:*\n https://vimeo.com/500390964?share=copy\n
*שיעור 4 – פתרון שאלות עם טבלה דו מימדית:*\n https://vimeo.com/500405510?share=copy\n
*שיעור 5 – הסתברות מותנית:*\n https://vimeo.com/500419278?share=copy\n"
"""


TRIGONOMETRY_LESSONS = """*שיעור 1 – טריגונומטריה במשולש ישר זווית:*\n https://vimeo.com/502188394?share=copy\n
*שיעור 2 – משפט הסינוסים:*\n https://vimeo.com/502199644?share=copy\n
*שיעור 3 – משפט הקוסינוסים:*\n https://vimeo.com/502353157?share=copy\n
*שיעור 4 – שטח משולש ומרובע בטריגו:*\n https://vimeo.com/502364902?share=copy\n"""


INTEGRALS_LESSONS = """*שיעור 1 – אינטגרל של פולינום ופונקציית מנה:*\n https://vimeo.com/498737441?share=copy\n
*שיעור 2 – אינטגרל פונ' שורש וטריגונומטריות:*\n https://vimeo.com/497585241?share=copy\n
*שיעור 3 – אינטגרל לפי זיהוי הנגזרת הפנימית:*\n https://vimeo.com/497897315?share=copy\n
*שיעור 4 – אינטגרל על ידי חילוק פולינומים:*\n https://vimeo.com/497897659?share=copy\n
*שיעור 5 – מציאת פונקציה בעזרת אינטגרל:*\n https://vimeo.com/498633380?share=copy\n
*שיעור 6 – חישוב שטחים בפולינומים:*\n https://vimeo.com/498633655?share=copy\n
*שיעור 7 – שטחים בפונ' מנה, שורש וטריגו:*\n https://vimeo.com/498634054?share=copy\n
*שיעור 8 – חישוב נפח גוף סיבוב בעזרת אינגרל:*\n https://vimeo.com/498634372?share=copy\n"""


RATIONALS_FUNCTIONS_LESSONS =  """*שיעור 1 – חוקי נגזרות:*\n https://vimeo.com/496637296?share=copy\n
*שיעור 2 – תחום הגדרה של פונקציית מנה:*\n https://vimeo.com/496646541?share=copy\n
*שיעור 3 – נגזרת ומשיק של פונקציית מנה:*\n https://vimeo.com/496647179?share=copy\n
*שיעור 4 – נקודות קיצון של פונקציית מנה:*\n https://vimeo.com/496647658?share=copy\n
*שיעור 5 – אסימפטוטות של פונקציית מנה:*\n https://vimeo.com/498742280?share=copy\n
*שיעור 6 – חקירת פונקציית מנה:*\n https://vimeo.com/496648963?share=copy\n"""


WORD_PROBLEMS_COMMUNITY = "https://t.me/+MzSKd_zCy6RjZjRk"


TRIGONOMETRY_FUNCTIONS_COMMUNITY = "https://t.me/+DD5zCpY7ds1lN2Y8"


ROOT_FUNCTIONS_COMMUNITY = "https://t.me/+meUrJgeRK1M4MWY0"


RATIONALS_FUNCTIONS_COMMUNITY = "https://t.me/+vsOqZ-TemPdmODQ0"    


SERIES_COMMUNITY = "https://t.me/+micA-c8i3NZkNjBk"


GEOMETRY_COMMUNITY = "https://t.me/+IWFu9KUd3PQ0MDM0"


TRIGONOMETRY_COMMUNITY = "https://t.me/+pLkwLfPtzhVkZWFk"


PROPABILITY_COMMUNITY = "https://t.me/+O0TZmFkosco2YWFk"


INTEGRALS_COMMUNITY = "https://t.me/+SBCz8iYpXlY3Nzk0"


PROPABILITY_PROGRAM = "https://drive.google.com/file/d/17BK4CB2NMcd_Q43NfdccfOPE793SsUYP/view?usp=sharing"


TRIGONOMETRY_PROGRAM = "https://drive.google.com/file/d/1DRAmcVSg-O67WCJg-9OraDBI7a4gy-07/view?usp=sharing"


ROOT_FUNCTIONS_PROGRAM = "https://drive.google.com/file/d/1JYX6fCfqoZ3JmxzsnpMFK-d4IA-7Pavj/view?usp=sharing"


RATIONALS_FUNCTIONS_PROGRAM = "https://drive.google.com/file/d/1giOPgWPW81_0j2LbtZIi7cGFxCL85Ycq/view?usp=sharing"


SERIES_PROGRAM = "https://drive.google.com/file/d/1Ey1VTUppfyqeXZ1pzPn__u0VX1P5WssR/view?usp=sharing"


GEOMETRY_PROGRAM = "https://drive.google.com/file/d/1ZYWPwSlsRU5KMja6A_5NzkmnByrrBJTg/view?usp=sharing"


TRIGONOMETRY_FUNCTIONS_PROGRAM = "https://drive.google.com/file/d/1iVRnorbj813Et4LfQq8Qd1m_l2wgorh5/view?usp=sharing"


WORD_PROBLEMS_PROGRAM = "https://drive.google.com/file/d/1p1H2x-vdMk-vehw0sjbneoMhz3kCwhgs/view?usp=sharing"


INTEGRALS_PROGRAM = "https://drive.google.com/file/d/1xufHYJNfAVmUi-5M3aqkA54ZQ7zM0pdk/view?usp=sharing"


PAST_EXAMS = """קיץ 2022: https://drive.google.com/file/d/1y95iihq-oO0qBFoeCRQsCcGL_SYYahMJ/view?usp=drive_link\n
קיץ 2022 מועד ב: https://drive.google.com/file/d/1Hn6p2DczQQ6gvxwJ-JoPFiN8nIs_OnDf/view?usp=sharing\n
קיץ 2023: https://drive.google.com/file/d/1YgwTK09M8VhHMklj76EPGO3_pzy_Bjpa/view?usp=sharing\n
קיץ 2023 מועד ב: https://drive.google.com/file/d/17-l2-x8VkItrM8yHA3z3O5ZFA2GbPxs-/view?usp=sharing\n
חורף 2023: https://drive.google.com/file/d/1RfZU3YXQZCVE8b0UBGHHjIPCn3F6zzUO/view?usp=sharing"""