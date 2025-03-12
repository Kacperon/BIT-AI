# FastAPI Game API

## Opis

Jest to API stworzone przy użyciu FastAPI, które implementuje mechanikę gry planszowej z obsługą różnych algorytmów AI, takich jak Minimax i Monte Carlo.

## Instalacja

Aby uruchomić API, należy zainstalować wymagane zależności:

```bash
pip install fastapi uvicorn
```

Następnie można uruchomić serwer za pomocą:

```bash
uvicorn main:app --reload
```

## Endpointy

### 1. `POST /start_game`
**Opis**: Inicjalizuje nową grę.

**Parametry**:
- `n` (int) - Rozmiar planszy.

**Zwraca**:
- `game` (list) - Stan początkowy gry.

### 2. `POST /get_valid_moves`
**Opis**: Zwraca listę możliwych ruchów dla gracza.

**Parametry**:
- `tab` (list) - Aktualny stan gry.
- `player` (int) - Numer gracza.

**Zwraca**:
- `valid_moves` (list) - Lista dostępnych ruchów.

### 3. `POST /make_move`
**Opis**: Wykonuje ruch gracza.

**Parametry**:
- `tab` (list) - Aktualny stan gry.
- `move` (tuple) - Wykonywany ruch.
- `player` (int) - Numer gracza.

**Zwraca**:
- `new_game_state` (list) - Nowy stan gry.
- `winner` (int) - Numer zwycięzcy lub 0, jeśli gra trwa.

### 4. `POST /generate_move_minmax`
**Opis**: Generuje najlepszy ruch dla gracza przy użyciu algorytmu Minimax.

**Parametry**:
- `game` (list) - Aktualny stan gry.
- `depth` (int) - Głębokość analizy.
- `if_alphabeta` (bool) - Czy używać optymalizacji Alfa-Beta.

**Zwraca**:
- `best_move` (tuple) - Najlepszy ruch.

### 5. `POST /generate_move_monte_carlo`
**Opis**: Generuje najlepszy ruch dla gracza przy użyciu algorytmu Monte Carlo.

**Parametry**:
- `game` (list) - Aktualny stan gry.
- `time` (int) - Limit czasu analizy.

**Zwraca**:
- `best_move` (tuple) - Najlepszy ruch.

## Autor
Projekt został stworzony w celu demonstracji algorytmów sztucznej inteligencji w grach planszowych. Możesz dostosować go do własnych potrzeb i rozwijać dalej!

