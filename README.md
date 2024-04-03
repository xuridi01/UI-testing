# ITS Projekt 1

- **Autor:** Mikuláš Uřídil (xuridi01)
- **Datum:** 2024-04-03

## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | x | x | x |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Search | x | x |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Filtred products |   |   | x | x |   |   |   |   |   |   |   |   |   |   |   |   |
| Detailed product |   |   |   | x | x | x |   |   |   |   |   |   |   |   |   |   |
| Shopping cart |   |   |   |   |   |   | x | x |   |   |   |   |   |   |   |   |
| Checkout |   |   |   |   |   |   |   | x | x |   |   |   |   |   |   |   |
| Admin Home |   |   |   |   |   |   |   |   |   | x |   |   |   |   |   |   |
| Admin Products |   |   |   |   |   |   |   |   |   | x | x | x | x | x | x | x |
| Admin Edit Product |   |   |   |   |   |   |   |   |   |   |   |   |   | x | x | x |
| Admin Add Product |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |   |


## Matice pokrytí aktivit

| Activities | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Find a product| x | x | x |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Show detailed product |   |   |   | x |   |   |   |   |   |   |   |   |   |   |   |   |
| Put product into the shopping cart |   |   |   |   | x | x | x |   |   |   |   |   |   |   |   |   |
| Buy a product |   |   |   |   |   |   | x | x | x |   |   |   |   |   |   |   |
| Admin lists products |   |   |   |   |   |   |   |   |   | x | x | x | x | x | x | x |
| Admin adds new product |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |   |
| Admin deletes product |   |   |   |   |   |   |   |   |   |   |   | x |   |   |   |   |
| Admin filters products |   |   |   |   |   |   |   |   |   |   |   |   | x |   |   |   |
| Admin edits product |   |   |   |   |   |   |   |   |   |   |   |   |   | x | x | x |


## Matice Feature-Test

| Feature file | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| search_and_buy.feature | x | x | x | x | x | x | x | x | x |   |   |   |   |   |   |   |
| prodict_management_and_storage.feature |   |   |   |   |   |   |   |   |   | x | x | x | x | x | x | x |
