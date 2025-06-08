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
      <Text style={styles.prediction}>{stock.prediction}</Text>
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
});

export default StockCard;
