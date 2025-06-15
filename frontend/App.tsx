import React from 'react';
import HomeScreen from './src/screens/HomeScreen';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import PredictionScreen from './src/screens/PredictionScreen';
import { Stock } from './src/data/mockStocks';

export type RootStackParamList = {
  Home: undefined;
  Prediction: { stock: Stock };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Prediction" component={PredictionScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};


export default App;
