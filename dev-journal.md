## [2025-06-12]
### File: App.tsx (Defines the app entry point and navigation.)
- 🔧 Refactored App.tsx to accomodate newly added prediction screen.
- ✅ Reason: Each pallete on clicked will have a new screen dedicated that will have all the data regarding its stock.

### File: /src/components/StockCard.tsx
- 🧹 Added stock price and upper cased the prediction
- ✅ Reason: Cleaner and styled UI.

### File:  /src/screens/HomeScreen.tsx
- 🔧 Changed the entire code of this file..earlier it used to support just the homescreen, but now will support prediction page too
- ✅ Reason: Added the prediction page too.

### File:  /src/screens/PredictionScreen.tsx
- 🔧 Added this to add more details regarding a particular stock
- ✅ Reason: Will bring in more data from the backend and other sources and will process it and display it here

