# Python_ollama_FastAPI
By Fabrizio Radica 2025

# Ollama Chat API

Un'API semplice creata con FastAPI per interagire con i modelli di linguaggio di Ollama. Questo servizio permette di generare risposte da modelli come Llama 3.1 attraverso chiamate API.

## Descrizione

Questo script crea un'API web che funge da intermediario tra l'utente e Ollama. L'API consente di inviare prompt a modelli di linguaggio ospitati localmente tramite Ollama e ricevere le relative risposte.

## Requisiti

- Python 3.7+
- Ollama installato e configurato sul sistema
- I seguenti pacchetti Python:
  - fastapi
  - uvicorn (per eseguire l'applicazione)
  - requests
  - pydantic
  - ollama (client Python per Ollama)

## Installazione

1. Clona questo repository:
   ```
   git clone https://github.com/username/ollama-chat-api.git
   cd ollama-chat-api
   ```

2. Installa le dipendenze:
   ```
   pip install fastapi uvicorn requests pydantic ollama
   ```

3. Assicurati che Ollama sia installato e in esecuzione sul tuo sistema. Se non l'hai ancora installato, segui le istruzioni su [ollama.ai](https://ollama.ai/).

4. Verifica che il modello "llama3.1" (o qualsiasi altro modello specificato come default) sia stato scaricato tramite Ollama. In caso contrario, puoi scaricarlo con:
   ```
   ollama pull llama3.1
   ```

## Utilizzo

### Avvio del server

Per avviare il server API:

```
uvicorn main:app --reload
```

Dove `main` è il nome del file Python contenente il codice. Il server sarà accessibile all'indirizzo `http://127.0.0.1:8000`.

### Endpoint disponibili

1. **Home** - `GET /`
   - Restituisce un semplice messaggio di benvenuto
   - Esempio: `http://127.0.0.1:8000/`

2. **Generate** - `GET /generate`
   - Genera una risposta dal modello Ollama
   - Parametri query:
     - `api_prompt`: Il messaggio da inviare al modello (default: "Ciao come ti chiami?")
     - `api_model`: Il modello Ollama da utilizzare (default: "llama3.1")
   - Esempio: `http://127.0.0.1:8000/generate?api_prompt=Qual%20è%20la%20capitale%20dell%27Italia?&api_model=llama3.1`

## Esempio di utilizzo tramite browser

1. Apri il tuo browser e vai all'indirizzo `http://127.0.0.1:8000/` per verificare che il servizio sia attivo.
2. Per generare una risposta, visita:
   ```
   http://127.0.0.1:8000/generate?api_prompt=Ciao, raccontami una storia breve
   ```
3. Il browser mostrerà la risposta generata dal modello Ollama. In questo caso, il modello risponderà come "Gigi", un assistente cordiale e preparato.

## Esempio di utilizzo tramite curl

```bash
curl "http://127.0.0.1:8000/generate?api_prompt=Ciao,%20come%20stai%20oggi?&api_model=llama3.1"
```

## Personalizzazione

- **System Prompt**: Nel codice è definito un system prompt che istruisce il modello a chiamarsi "Gigi". Puoi modificare questa istruzione nel codice.
- **Modello Default**: Il modello predefinito è "llama3.1", ma puoi utilizzare qualsiasi modello disponibile in Ollama.

## Note tecniche

- L'API utilizza FastAPI per creare un servizio web leggero e performante
- La comunicazione con Ollama avviene tramite il client Python ufficiale
- Le risposte sono restituite in formato testo semplice
- È implementata la gestione degli errori per gestire problemi di comunicazione con Ollama

## Risoluzione dei problemi

- Assicurati che Ollama sia in esecuzione prima di avviare il server API
- Verifica che il modello specificato (es. "llama3.1") sia stato scaricato da Ollama
- Se ricevi errori 500, controlla il log del server per dettagli sull'errore

## Licenza

Questo progetto è rilasciato come Free Open Source Software. Sei libero di utilizzare, modificare e distribuire questo codice per qualsiasi scopo, inclusi scopi commerciali, senza alcuna restrizione.

## Contribuire

I contributi sono benvenuti! Sentiti libero di aprire issues o pull requests.

<a href="https://www.buymeacoffee.com/fabbroz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=fabbroz&button_colour=FF5F5F&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>
