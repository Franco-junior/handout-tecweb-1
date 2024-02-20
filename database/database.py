import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, nome_banco) -> None:
        self.conn = sqlite3.connect(nome_banco + '.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            content TEXT NOT NULL );''')
    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES (?, ?);", (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        self.notes = []
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in self.cursor:
            ident, titulo, conteudo = linha[0], linha[1], linha[2]
            self.notes.append(Note(id=ident,title=titulo, content=conteudo))
        return self.notes
    
    def update(self, entry):
        self.conn.execute("UPDATE note SET content = (?) WHERE id = (?);", (entry.content, entry.id))
        self.conn.execute("UPDATE note SET title = (?) WHERE id = (?);", (entry.title, entry.id))
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = (?);", (str(note_id)))
        self.conn.commit()