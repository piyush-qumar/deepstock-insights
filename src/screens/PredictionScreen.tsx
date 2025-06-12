import React from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import { Stock, StockPrediction } from "../data/mockStocks";
import StockCard from "../components/StockCard";
import { RouteProp } from '@react-navigation/native';
import { useNavigation } from "@react-navigation/native";
import { StackNavigationProp } from "@react-navigation/stack";
import { useTheme } from "@react-navigation/native";

type RootStackParamList = {
  Home: undefined;
  Prediction: { stock: Stock };
};

type PredictionScreenRouteProp = RouteProp<RootStackParamList, 'Prediction'>;

interface Props {
  route: PredictionScreenRouteProp;
}

const PredictionScreen: React.FC<Props> = ({ route }) => {
  const { stock } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{stock.name}</Text>
      <Text style={styles.subtitle}>Symbol: {stock.symbol}</Text>
      <Text>Prediction: {stock.prediction}</Text>
      {/* Placeholder: will show chart later */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold' },
  subtitle: { fontSize: 18, marginVertical: 10 },
});

export default PredictionScreen;