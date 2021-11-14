import discord
from discord.ext import commands
from pythonpancakes import PancakeSwapAPI
from pycoingecko import CoinGeckoAPI as cg
import datetime
import requests

#configs
ps = PancakeSwapAPI()
price_brl = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL')
price_brl_data = price_brl.json()
price_brl = price_brl_data.get('price')

class Symbol(commands.Cog):
    """ Works with cryptocurrencies """

    def __init__(self, client):
        self.client = client

    @commands.command(name='symbol')
    async def symbol(self, ctx, symbol, total='1'):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        symbol = symbol.upper()
        if symbol == 'YEL':
            contract_address = '0xd3b71117e6c1558c1553305b44988cd944e97300'
            exchange = 'PancakeSwap'
        if symbol == 'BFC':
            contract_address = '0x727b531038198e27a1a4d0fd83e1693c1da94892'
            exchange = 'PancakeSwap'
        if symbol == 'GOLD':
            contract_address = '0xb3a6381070b1a15169dea646166ec0699fdaea79'
            exchange = 'PancakeSwap'
        if symbol == 'PMON':
            contract_address = '0x1796ae0b0fa4862485106a0de9b654efe301d0b2'
            exchange = 'PancakeSwap'
        if symbol == 'PVU':
            contract_address = '0x31471e0791fcdbe82fbf4c44943255e923f1b794'
            exchange = 'PancakeSwap'
        if symbol == 'HERO':
            contract_address = '0xd40bedb44c081d2935eeba6ef5a3c8a31a1bbe13'
            exchange = 'PancakeSwap'
        if symbol == 'SLP':
            contract_address = '0x070a08beef8d36734dd67a491202ff35a6a16d97'
            exchange = 'PancakeSwap'
        if symbol == 'CARDANO':
            contract_address = '0x3ee2200efb3400fabb9aacf31297cbdd1d435d47'
            exchange = 'PancakeSwap'
        if symbol == 'DOGE':
            contract_address = '0xba2ae424d960c26247dd6c32edc70b295c744c43'
            exchange = 'PancakeSwap'
        if symbol == 'BNX':
            contract_address = '0x8c851d1a123ff703bd1f9dabe631b69902df5f97'
            exchange = 'PancakeSwap'
        if symbol == 'DOL':
            contract_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
            api_id = 'usd-coin'
            exchange = 'CoinGecko'
        if symbol == 'BNB':
            contract_address = None
            api_id = 'binancecoin'
            exchange = 'CoinGecko'

        if exchange == 'PancakeSwap':
            token = ps.tokens(contract_address)
            token = token.get('data', 'price')
            price = token.get('price')
            price_total = (float(price) * float(total))
            price_brltotal = (float(price) * float(price_brl)) * float(total)

            token_embed = discord.Embed(title='')
            token_embed = token_embed.add_field(name='Quantidade de tokens:', value=f'{total}', inline=False)
            token_embed = token_embed.add_field(name='Preço atual:', value=f'${price_total:.6f} | R${price_brltotal:.2f}', inline=False)
            token_embed = token_embed.add_field(name='Contrato:', value=f'{contract_address}')
            token_embed = token_embed.set_footer(text=f'{exchange} | {now}', icon_url=f'https://img1.gratispng.com/20180330/eje/kisspng-bitcoin-cryptocurrency-monero-initial-coin-offerin-bitcoin-5abdfe6b6c5365.2052061515224008754437.jpg')
            await ctx.send(embed=token_embed)

        if exchange == 'CoinGecko':
            token_cg = cg().get_price(f'{api_id}', 'usd')
            token_cg = token_cg.get(f'{api_id}', 'usd')
            token_cg_price = token_cg.get('usd')
            token_cg_price = (float(token_cg_price))
            token_cg_brltotal = (float(token_cg_price) * float(price_brl) * float(total))

            token_embed_cg = discord.Embed(title='')
            token_embed_cg = token_embed_cg.add_field(name='Quantidade de tokens:', value=f'{total}', inline=False)
            token_embed_cg = token_embed_cg.add_field(name='Preço atual:', value=f'${token_cg_price:.6f} | R${token_cg_brltotal:.2f}', inline=False)
            token_embed_cg = token_embed_cg.add_field(name='Contrato:', value=contract_address)
            token_embed_cg = token_embed_cg.set_footer(text=f'{exchange} | {now}', icon_url=f'https://img1.gratispng.com/20180330/eje/kisspng-bitcoin-cryptocurrency-monero-initial-coin-offerin-bitcoin-5abdfe6b6c5365.2052061515224008754437.jpg')
            await self.client.ctx.send(embed=token_embed_cg)

def setup(client):
    client.add_cog(Symbol(client))
