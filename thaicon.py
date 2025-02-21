import tkinter as tk
import random

# Complete list of Thai consonants with their names
thai_consonants = [
    ("ก", "Gor Gai (กอไก่)"), ("ข", "Khor Khai (ขอไข่)"), ("ฃ", "Khor Khuat (ขอขวด)"),
    ("ค", "Kor Khuat (คอขวด)"), ("ฅ", "Khor Khon (คอคน)"), ("ฆ", "Khor Rakhang (คอระฆัง)"),
    ("ง", "Ngor Ngu (งองู)"), ("จ", "Jor Jan (จอจาน)"), ("ฉ", "Chor Ching (ฉอฉิ่ง)"),
    ("ช", "Chor Chang (ชอช้าง)"), ("ซ", "Sor So (ซอโซ่)"), ("ฌ", "Chor Choe (ฌอเฌอ)"),
    ("ญ", "Yor Ying (ญอหญิง)"), ("ฎ", "Dor Chada (ฎอชฎา)"), ("ฏ", "Tor Patak (ฏอปฏัก)"),
    ("ฐ", "Thor Than (ฐอฐาน)"), ("ฑ", "Thor Montho (ฑอมนโท)"), ("ฒ", "Thor Phu Thao (ฒอผู้เฒ่า)"),
    ("ณ", "Nor Nen (ณอเณร)"), ("ด", "Dor Dek (ดอเด็ก)"), ("ต", "Tor Tao (ตอเต่า)"),
    ("ถ", "Thor Thung (ถอถุง)"), ("ท", "Thor Thahan (ทอทหาร)"), ("ธ", "Thor Thong (ธอธง)"),
    ("น", "Nor Nu (นอหนู)"), ("บ", "Bor Baimai (บอใบไม้)"), ("ป", "Por Pla (ปอปลา)"),
    ("ผ", "Phor Phung (ผอผึ้ง)"), ("ฝ", "For Fa (ฝอฟัน)"), ("พ", "Por Pha (พอพาน)"),
    ("ฟ", "For Fun (ฟอฟัน)"), ("ภ", "Por Sampao (ภอสำเภา)"), ("ม", "Mor Ma (มอม้า)"),
    ("ย", "Yor Yak (ยอยักษ์)"), ("ร", "Ror Rua (รอเรือ)"), ("ฤ", "Lor Ling (ลอลิง)"),
    ("ล", "Lor Chula (ฬอจุฬา)"), ("ฦ", "Sor Sala (สอศาลา)"), ("ว", "Sor Rue Si (สอฤาษี)"),
    ("ศ", "Sor Suea (สอเสือ)"), ("ษ", "Hor Hip (หอหีบ)"), ("ส", "Lor Chula (ฬอจุฬา)"),
    ("ห", "Or Ang (อออ่าง)"), ("ฬ", "Hor Nokhuk (ฮอนกฮูก)")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        self.is_flipped = False
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white")
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=5)
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.is_flipped = False
        self.label.config(text=self.current_card[0])
    
    def flip_card(self):
        if self.current_card:
            if not self.is_flipped:
                self.label.config(text=self.current_card[1])
                self.is_flipped = True
            else:
                self.label.config(text=self.current_card[0])
                self.is_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

