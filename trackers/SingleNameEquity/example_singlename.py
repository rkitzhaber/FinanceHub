from trackers import SingleNameEquity
import matplotlib.pyplot as plt

sne = SingleNameEquity('AAPL US Equity')
# sne = SingleNameEquity('PETR4 BZ Equity')

sne.ts_df[['Dividend']].plot()
plt.show()

sne.ts_df[['Quantity']].plot()
plt.show()

sne.ts_df[['Price', 'Total Return Index']].plot()
plt.show()
