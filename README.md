Backend dla zadania rekrutacyjnego. Treść zadania:

# Treść zadania

Firma Potato, pod kierownictwem Jeve’a Stobsa wkrótce przedstawi super innowacyjny czat wykorzystujący GPT-3. Niemniej jednak, jak na każdej prezentacji, software nie jest jeszcze wystarczająco gotowy do działania. Trzeba zatem napisać demo, które idealnie odwzoruje funkcjonalność tego czatu na potrzeby prezentacji.

Twoim zadaniem jest uratowanie prezentacji Jeve’a poprzez napisanie aplikacji do czatu „symulującej” sztuczną inteligencję. Firma przygotowała listę kilku tysięcy wiadomości i odpowiedzi. Na każdą z wiadomości „sztuczna inteligencja” powinna odpowiedzieć zgodnie z przygotowaną listą. W przypadku otrzymania wiadomości spoza listy powinna odpowiedzieć „More information in Potato Chat Premium!”.

# Wymagania funkcjonalne
Twoja aplikacja powinna działać w następujący sposób:

1. Istnieje jeden pokój czatu, do którego można dołączyć bez żadnej autoryzacji. Jego URL jest znany osobie wchodzącej.
2. Osoby powinny widzieć wiadomości w całym pokoju oraz odpowiedzi od Potato Chatu
3. Osoby nie będą się identyfikować, każdy dołącza jako anonimowy użytkownik. Sztuczna inteligencja identyfikuje się jako Potato Chatbot
4. Serwer powinien przechowywać historię czatu.
5. Czat powinien odpowiadać niezależnie od wielkości wpisanych liter i spacji w pytaniu

##### Przykład
Jeśli pytanie istnieje w zbiorze, to czat powinien odpowiedzieć na poniższe pytania w taki sam sposób:
<pre>Pytanie         pierwsze    -   DaJ mI OdPoWiedŹ</pre>
<pre>Pytanie pierwsze - daj mi odpowiedź</pre>

6. Wysłanie wiadomości powinno odbyć się z pomocą klawisza Enter. Nie musisz martwić się o wielolinijkowość. Sztuczna inteligencja rozumie tylko jedną linijkę.
7. Wiadomość powinna zawierać:
    - Autora (Czy to anonimowy użytkownik czy sztuczna inteligencja)
    - Datę i godzinę wysłania (wyświetlane wg strefy czasowej użytkownika, czyli jeśli ktoś wysyła do mnie wiadomość w czasie amerykańskim, a ja ją otrzymuje w Polsce, to datę wysyłki chcę widzieć w czasie lokalnym w Polsce)
    - Treść
8. Dane z pytaniami, na które ma odpowiadać Potato Chat znajdują się w katalogu `data` w pliku `questions_answers.json` i mogą oczywiście zmienić swoje położenie.

# Wymagania niefunkcjonalne
1. Nie musisz martwić się o style, hipsterski HTML z lat 90 jest bardzo trendy.

*****

# Wskazówki
1. **NIE MUSISZ** pisać testów do tego zadania.
2. Możesz korzystać z dowolnych bibliotek.
2. Użycie bazy danych do hostowania odpowiedzi chatbota jest opcjonalne.
3. Reset repozytorium do stanu początkowego - `git clean -fdx && git reset --hard`
4. Aplikacja nie musi być przygotowana do uruchomienia w skompilowanej formie. Wystarczy, że będzie działać w środowisku developerskim.

# Uruchomienie aplikacji
## 0. Stack narzędziowy konieczny do uruchomienia
- node 16 (https://nodejs.org/en/download/) - sprawdzono działanie na 16.17.0
- npm 8.19 (https://www.npmjs.com/get-npm) - sprawdzono działanie na 8.19.2
- git (https://git-scm.com/downloads)
- Python oraz Django (w dowolnej wersji)

## 1. Potato Chat Client
Dla ułatwienia dostarczamy początkowy kod dla aplikacji frontendowej w katalogu `potato-chat-client`. Aby go uruchomić należy wykonać następujące kroki:
1. `cd potato-chat-client`
2. `npm install`
3. `npm start`
4. Aplikacja powinna być dostępna pod adresem `http://localhost:3000`
5. Aplikacja spodziewa się serwera pod adresem znajdującym się w pliku `src/config.ts` (domyślnie `http://localhost:8000`)
   Aplikacja próbuje domyślnie próbuje się połączyć z endpointem `/ChatMessages`, który jeszcze nie istnieje.

## 2. Potato Chat Server
Do zaimplementowania Potato Chat Server użyj Pythona oraz Django.

# FAQ:
#### Jak ustawić port, z którym powinien kontaktować się klient?
- Port można zmienić w pliku `potato-chat-client/src/config.ts` w zmiennej `SERVER_URL`.
#### Nie mogę zainstalować pakietów.
- Jeśli posiadasz zestaw narzędzi wylistowany w punkcie 0 i problem występuje, niezwłocznie się z nami skontaktuj, wysyłając zrzuty ekranów z wersjami zainstalowanych narzędzi.