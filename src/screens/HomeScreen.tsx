import React from 'react';
import { FlatList, View, StyleSheet, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { RootStackParamList } from '../../App';
import StockCard from '../components/StockCard';
import { mockStocks } from '../data/mockStocks';



const HomeScreen = () => {
  const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList, 'Home'>>();
  return (
    <View style={styles.container}>
      <FlatList
        data={mockStocks}
        keyExtractor={(item) => item.symbol}
        renderItem={({ item }) => <TouchableOpacity onPress={() => navigation.navigate('Prediction', { stock: item })}><StockCard stock={item} /></TouchableOpacity>} 
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
