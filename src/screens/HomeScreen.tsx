import React from 'react';
import { FlatList, View, StyleSheet } from 'react-native';
import StockCard from '../components/StockCard';
import { mockStocks } from '../data/mockStocks';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <FlatList
        data={mockStocks}
        keyExtractor={(item) => item.symbol}
        renderItem={({ item }) => <StockCard stock={item} />}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
});

export default HomeScreen;
