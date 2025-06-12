import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Stock, StockPrediction } from '../data/mockStocks';

interface Props {
  stock: Stock;
}

const StockCard: React.FC<Props> = ({ stock }) => {
  const getStyle = () => {
    switch (stock.prediction) {
      case 'bullish':
        return styles.up;
      case 'bearish':
        return styles.down;
      case 'neutral':
      default:
        return styles.neutral;
    }
  };

  return (
    <View style={[styles.card, getStyle()]}>
      <Text style={styles.name}>{stock.name}</Text>
      <Text style={styles.price}>${stock.price.toFixed(2)} ({stock.change > 0 ? '+' : ''}{stock.change.toFixed(2)}%)</Text>
      {/* Prediction can be displayed in uppercase for better visibility */}
      <Text style={styles.prediction}>{stock.prediction.toUpperCase()}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    padding: 16,
    margin: 10,
    borderRadius: 10,
    backgroundColor: '#fff',
    elevation: 4,
  },
  name: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  prediction: {
    fontSize: 16,
    marginTop: 8,
    textTransform: 'uppercase',
  },
  up: {
    borderLeftWidth: 5,
    borderLeftColor: 'green',
  },
  down: {
    borderLeftWidth: 5,
    borderLeftColor: 'red',
  },
  neutral: {
    borderLeftWidth: 5,
    borderLeftColor: 'gray',
  },
  price: {
    fontSize: 16,
    color: '#333',
  },
});

export default StockCard;
