import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [tipoCarro, setTipoCarro] = useState<string>('hatch');
  const [anoCarro, setAnoCarro] = useState<number | string>('');
  const [desconto, setDesconto] = useState<number | null>(null);

  const calcularDesconto = () => {
    const ano = typeof anoCarro === 'string' ? parseInt(anoCarro) : anoCarro;
    
    if (isNaN(ano)) {
      setDesconto(null);
      return;
    }

    let descontoCalculado = 0;

    if (tipoCarro === 'hatch') {
      if (ano >= 2012) {
        descontoCalculado = 10;
      } else if (ano >= 2007 && ano <= 2011) {
        descontoCalculado = 15;
      } else if (ano < 2007) {
        descontoCalculado = 19;
      }
    } else if (tipoCarro === 'sedã') {
      if (ano >= 2012) {
        descontoCalculado = 8;
      } else if (ano >= 2007 && ano <= 2011) {
        descontoCalculado = 12;
      } else if (ano < 2007) {
        descontoCalculado = 20;
      }
    }

    setDesconto(descontoCalculado);
  };

  return (
    <div className="App">
      <h1>Sistema de Desconto de Veículos</h1>

      <div>
        <label>Selecione o tipo de carro:</label>
        <select value={tipoCarro} onChange={(e) => setTipoCarro(e.target.value)}>
          <option value="hatch">Hatch</option>
          <option value="sedã">Sedã</option>
        </select>
      </div>

      <div>
        <label>Informe o ano do veículo:</label>
        <input
          type="number"
          value={anoCarro}
          onChange={(e) => setAnoCarro(e.target.value)}
          placeholder="Ex: 2010"
        />
      </div>

      <button onClick={calcularDesconto}>Calcular Desconto</button>

      {desconto !== null && (
        <div className="result">
          <h2>Desconto Aplicado</h2>
          <p>O desconto aplicado é de {desconto}%.</p>
        </div>
      )}
    </div>
  );
};

export default App;