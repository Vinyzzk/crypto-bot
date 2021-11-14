"""
    Crypto Bot - Working on cryptocurrencies
"""
import discord
import datetime
import requests
import random
from pythonpancakes import PancakeSwapAPI
from pycoingecko import CoinGeckoAPI as cg
from discord.ext import commands, tasks
from requests.api import request
from requests.models import Response

ps = PancakeSwapAPI()

client = commands.Bot('$')

#   PRICE BRL
price_brl = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL')
price_brl_data = price_brl.json()
price_brl = price_brl_data.get('price')

@client.event
async def on_ready():
    print('Online.')
    current_prices.start()
    gerin_calls.start()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'caralsssho' in message.content:
        await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários.')
        await message.delete()

    if 'pvu' in message.content:
        nr = random.randint(1,3)
        if nr == 3:
            await message.channel.send(':rocket: PVU é lua :rofl: :clown:')

    await client.process_commands(message)

@tasks.loop(seconds=1800)
async def gerin_calls():
    channel = client.get_channel(901965451742027838)
    lista = ['Call do rogério? :cold_face: ', ':rocket: <:pvu:905546765330182194> PVU é lua :new_moon: :clown: :rofl:']
    nr = random.randint(1,6)
    if nr == 6:
        await channel.send(random.choice(lista))

@tasks.loop(seconds=300)
async def current_prices():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = client.get_channel(905272951526555678)

    # PancakeSwap API
    token_yel = ps.tokens('0xd3b71117e6c1558c1553305b44988cd944e97300')
    token_yel_price = token_yel.get('data', 'price')
    token_yel_price = token_yel_price.get('price')
    token_yelbrl_price = (float(token_yel_price) * float(price_brl))
    token_yel_text = f'${float(token_yel_price):.6f} | R${float(token_yelbrl_price):.2f}'

    token_bfc = ps.tokens('0x727b531038198e27a1a4d0fd83e1693c1da94892')
    token_bfc_price = token_bfc.get('data', 'price')
    token_bfc_price = token_bfc_price.get('price')
    token_bfcbrl_price = (float(token_bfc_price) * float(price_brl))
    token_bfc_text = f'${float(token_bfc_price):.6f} | R${float(token_bfcbrl_price):.2f}'

    token_gold = ps.tokens('0xb3a6381070b1a15169dea646166ec0699fdaea79')
    token_gold_price = token_gold.get('data', 'price')
    token_gold_price = token_gold_price.get('price')
    token_goldbrl_price = (float(token_gold_price) * float(price_brl))
    token_gold_text = f'${float(token_gold_price):.6f} | R${float(token_goldbrl_price):.2f}'

    token_pmon = ps.tokens('0x1796ae0b0fa4862485106a0de9b654efe301d0b2')
    token_pmon_price = token_pmon.get('data', 'price')
    token_pmon_price = token_pmon_price.get('price')
    token_pmonbrl_price = (float(token_pmon_price) * float(price_brl))
    token_pmon_text = f'${float(token_pmon_price):.6f} | R${float(token_pmonbrl_price):.2f}'

    token_pvu = ps.tokens('0x31471e0791fcdbe82fbf4c44943255e923f1b794')
    token_pvu_price = token_pvu.get('data', 'price')
    token_pvu_price = token_pvu_price.get('price')
    token_pvubrl_price = (float(token_pvu_price) * float(price_brl))
    token_pvu_text = f'${float(token_pvu_price):.6f} | R${float(token_pvubrl_price):.2f}'

    token_metahero = ps.tokens('0xd40bedb44c081d2935eeba6ef5a3c8a31a1bbe13')
    token_metahero_price = token_metahero.get('data', 'price')
    token_metahero_price = token_metahero_price.get('price')
    token_metaherobrl_price = (float(token_metahero_price) * float(price_brl))
    token_metahero_text = f'${float(token_metahero_price):.6f} | R${float(token_metaherobrl_price):.2f}'
    
    token_slp = ps.tokens('0x070a08beef8d36734dd67a491202ff35a6a16d97')
    token_slp_price = token_slp.get('data', 'price')
    token_slp_price = token_slp_price.get('price')
    token_slpbrl_price = (float(token_slp_price) * float(price_brl))
    token_slp_text = f'${float(token_slp_price):.6f} | R${float(token_slpbrl_price):.2f}'

    token_cardano = ps.tokens('0x3ee2200efb3400fabb9aacf31297cbdd1d435d47')
    token_cardano_price = token_cardano.get('data', 'price')
    token_cardano_price = token_cardano_price.get('price')
    token_cardanobrl_price = (float(token_cardano_price) * float(price_brl))
    token_cardano_text = f'${float(token_cardano_price):.6f} | R${float(token_cardanobrl_price):.2f}'

    token_dsbowl = ps.tokens('0x6a43f8f4b12fcd3b3eb86b319f92eb17c955dda3')
    token_dsbowl_price = token_dsbowl.get('data', 'price')
    token_dsbowl_price = token_dsbowl_price.get('price')
    token_dsbowlbrl_price = (float(token_dsbowl_price) * float(price_brl))
    token_dsbowl_text = f'${float(token_dsbowl_price):.6f} | R${float(token_dsbowlbrl_price):.2f}'

    token_binaryx = ps.tokens('0x8c851d1a123ff703bd1f9dabe631b69902df5f97')
    token_binaryx_price = token_binaryx.get('data', 'price')
    token_binaryx_price = token_binaryx_price.get('price')
    token_binaryxbrl_price = (float(token_binaryx_price) * float(price_brl))
    token_binaryx_text = f'${float(token_binaryx_price):.6f} | R${float(token_binaryxbrl_price):.2f}'

    # CoinGecko API

    token_mnstrs = cg().get_price('block-monsters', 'usd')
    token_mnstrs = token_mnstrs.get('block-monsters', 'usd')
    token_mnstrs_price = token_mnstrs.get('usd')
    token_brlmnstrs_price = (float(token_mnstrs_price) * float(price_brl))
    token_mnstrs_text = f'${float(token_mnstrs_price):.6f} | R${float(token_brlmnstrs_price):.2f}'

    token_btc = cg().get_price('bitcoin', 'usd')
    token_btc = token_btc.get('bitcoin', 'usd')
    token_btc_price = token_btc.get('usd')
    token_brlbtc_price = (float(token_btc_price) * float(price_brl))
    token_btc_text = f'R${float(token_brlbtc_price):.2f}'

    token_eth = cg().get_price('ethereum', 'usd')
    token_eth = token_eth.get('ethereum', 'usd')
    token_eth_price = token_eth.get('usd')
    token_brleth_price = (float(token_eth_price) * float(price_brl))
    token_eth_text = f'R${float(token_brleth_price):.2f}'

    token_bnb = cg().get_price('binancecoin', 'usd')
    token_bnb = token_bnb.get('binancecoin', 'usd')
    token_bnb_price = token_bnb.get('usd')
    token_brlbnb_price = (float(token_bnb_price) * float(price_brl))
    token_bnb_text = f'R${float(token_brlbnb_price):.2f}'

    token_mgpx = cg().get_price('monster-grand-prix-token', 'usd')
    token_mgpx = token_mgpx.get('monster-grand-prix-token', 'usd')
    token_mgpx_price = token_mgpx.get('usd')
    token_brlmgpx_price = (float(token_mgpx_price) * float(price_brl))
    token_mgpx_text = f'${float(token_mgpx_price):.6f} | R${float(token_brlmgpx_price):.2f}'

    token_ccar = cg().get_price('cryptocars', 'usd')
    token_ccar = token_ccar.get('cryptocars', 'usd')
    token_ccar_price = token_ccar.get('usd')
    token_brlccar_price = (float(token_ccar_price) * float(price_brl))
    token_ccar_text = f'${float(token_ccar_price):.6f} | R${float(token_brlccar_price):.2f}'

    embed = discord.Embed(title='')
    embed = embed.add_field(name='<:btc:905580814807478282> BTC:', value=token_btc_text)
    embed = embed.add_field(name='<:eth:905581264654958592> ETH:', value=token_eth_text)
    embed = embed.add_field(name='<:bnb:905581514367074324> BNB:', value=token_bnb_text)
    embed = embed.add_field(name='<:yel:905544368474165290> YEL:', value=token_yel_text)
    embed = embed.add_field(name='<:bfc:905580443108257862> BFC:', value=token_bfc_text)
    embed = embed.add_field(name='<:pvu:905546765330182194> PVU:', value=token_pvu_text)
    embed = embed.add_field(name='<:slp:905582281735954482> SLP:', value=token_slp_text)
    embed = embed.add_field(name='<:pmon:905582710058274816> PMON:', value=token_pmon_text)
    embed = embed.add_field(name='<:hero:905583274506723348> HERO:', value=token_metahero_text)
    embed = embed.add_field(name='<:cardano:905583427313602612> CARDANO:', value=token_cardano_text)
    embed = embed.add_field(name='<:MNSTRS:905583611410022410> MNSTRS:', value=token_mnstrs_text)
    embed = embed.add_field(name='<:dsbowl:905586282925801544> DOGE:', value=token_dsbowl_text)
    embed = embed.add_field(name='<:bnx:905584004718264410> BNX:', value=token_binaryx_text)
    embed = embed.add_field(name='<:bnx:905584004718264410> GOLD:', value=token_gold_text)
    embed = embed.add_field(name='<:mgpx:908143326191050842> MGPX:', value=token_mgpx_text)
    embed = embed.add_field(name='<:ccar:908147500911841300> CCAR:', value=token_ccar_text)
    embed = embed.add_field(name='EMPTY', value='EMPTY')

    embed = embed.set_footer(text=f'PancakeSwap & CoinGecko | {now}', icon_url=f'https://img1.gratispng.com/20180330/eje/kisspng-bitcoin-cryptocurrency-monero-initial-coin-offerin-bitcoin-5abdfe6b6c5365.2052061515224008754437.jpg')
    await channel.send(embed=embed)

@client.command(name='$')
async def all_values(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    # PancakeSwap API
    token_yel = ps.tokens('0xd3b71117e6c1558c1553305b44988cd944e97300')
    token_yel_price = token_yel.get('data', 'price')
    token_yel_price = token_yel_price.get('price')
    token_yelbrl_price = (float(token_yel_price) * float(price_brl))
    token_yel_text = f'${float(token_yel_price):.6f} | R${float(token_yelbrl_price):.2f}'

    token_bfc = ps.tokens('0x727b531038198e27a1a4d0fd83e1693c1da94892')
    token_bfc_price = token_bfc.get('data', 'price')
    token_bfc_price = token_bfc_price.get('price')
    token_bfcbrl_price = (float(token_bfc_price) * float(price_brl))
    token_bfc_text = f'${float(token_bfc_price):.6f} | R${float(token_bfcbrl_price):.2f}'

    token_gold = ps.tokens('0xb3a6381070b1a15169dea646166ec0699fdaea79')
    token_gold_price = token_gold.get('data', 'price')
    token_gold_price = token_gold_price.get('price')
    token_goldbrl_price = (float(token_gold_price) * float(price_brl))
    token_gold_text = f'${float(token_gold_price):.6f} | R${float(token_goldbrl_price):.2f}'

    token_pmon = ps.tokens('0x1796ae0b0fa4862485106a0de9b654efe301d0b2')
    token_pmon_price = token_pmon.get('data', 'price')
    token_pmon_price = token_pmon_price.get('price')
    token_pmonbrl_price = (float(token_pmon_price) * float(price_brl))
    token_pmon_text = f'${float(token_pmon_price):.6f} | R${float(token_pmonbrl_price):.2f}'

    token_pvu = ps.tokens('0x31471e0791fcdbe82fbf4c44943255e923f1b794')
    token_pvu_price = token_pvu.get('data', 'price')
    token_pvu_price = token_pvu_price.get('price')
    token_pvubrl_price = (float(token_pvu_price) * float(price_brl))
    token_pvu_text = f'${float(token_pvu_price):.6f} | R${float(token_pvubrl_price):.2f}'

    token_metahero = ps.tokens('0xd40bedb44c081d2935eeba6ef5a3c8a31a1bbe13')
    token_metahero_price = token_metahero.get('data', 'price')
    token_metahero_price = token_metahero_price.get('price')
    token_metaherobrl_price = (float(token_metahero_price) * float(price_brl))
    token_metahero_text = f'${float(token_metahero_price):.6f} | R${float(token_metaherobrl_price):.2f}'
    
    token_slp = ps.tokens('0x070a08beef8d36734dd67a491202ff35a6a16d97')
    token_slp_price = token_slp.get('data', 'price')
    token_slp_price = token_slp_price.get('price')
    token_slpbrl_price = (float(token_slp_price) * float(price_brl))
    token_slp_text = f'${float(token_slp_price):.6f} | R${float(token_slpbrl_price):.2f}'

    token_cardano = ps.tokens('0x3ee2200efb3400fabb9aacf31297cbdd1d435d47')
    token_cardano_price = token_cardano.get('data', 'price')
    token_cardano_price = token_cardano_price.get('price')
    token_cardanobrl_price = (float(token_cardano_price) * float(price_brl))
    token_cardano_text = f'${float(token_cardano_price):.6f} | R${float(token_cardanobrl_price):.2f}'

    token_dsbowl = ps.tokens('0x6a43f8f4b12fcd3b3eb86b319f92eb17c955dda3')
    token_dsbowl_price = token_dsbowl.get('data', 'price')
    token_dsbowl_price = token_dsbowl_price.get('price')
    token_dsbowlbrl_price = (float(token_dsbowl_price) * float(price_brl))
    token_dsbowl_text = f'${float(token_dsbowl_price):.6f} | R${float(token_dsbowlbrl_price):.2f}'

    token_binaryx = ps.tokens('0x8c851d1a123ff703bd1f9dabe631b69902df5f97')
    token_binaryx_price = token_binaryx.get('data', 'price')
    token_binaryx_price = token_binaryx_price.get('price')
    token_binaryxbrl_price = (float(token_binaryx_price) * float(price_brl))
    token_binaryx_text = f'${float(token_binaryx_price):.6f} | R${float(token_binaryxbrl_price):.2f}'

    # CoinGecko API

    token_mnstrs = cg().get_price('block-monsters', 'usd')
    token_mnstrs = token_mnstrs.get('block-monsters', 'usd')
    token_mnstrs_price = token_mnstrs.get('usd')
    token_brlmnstrs_price = (float(token_mnstrs_price) * float(price_brl))
    token_mnstrs_text = f'${float(token_mnstrs_price):.6f} | R${float(token_brlmnstrs_price):.2f}'

    token_btc = cg().get_price('bitcoin', 'usd')
    token_btc = token_btc.get('bitcoin', 'usd')
    token_btc_price = token_btc.get('usd')
    token_brlbtc_price = (float(token_btc_price) * float(price_brl))
    token_btc_text = f'R${float(token_brlbtc_price):.2f}'

    token_eth = cg().get_price('ethereum', 'usd')
    token_eth = token_eth.get('ethereum', 'usd')
    token_eth_price = token_eth.get('usd')
    token_brleth_price = (float(token_eth_price) * float(price_brl))
    token_eth_text = f'R${float(token_brleth_price):.2f}'

    token_bnb = cg().get_price('binancecoin', 'usd')
    token_bnb = token_bnb.get('binancecoin', 'usd')
    token_bnb_price = token_bnb.get('usd')
    token_brlbnb_price = (float(token_bnb_price) * float(price_brl))
    token_bnb_text = f'R${float(token_brlbnb_price):.2f}'

    token_mgpx = cg().get_price('monster-grand-prix-token', 'usd')
    token_mgpx = token_mgpx.get('monster-grand-prix-token', 'usd')
    token_mgpx_price = token_mgpx.get('usd')
    token_brlmgpx_price = (float(token_mgpx_price) * float(price_brl))
    token_mgpx_text = f'${float(token_mgpx_price):.6f} | R${float(token_brlmgpx_price):.2f}'

    token_ccar = cg().get_price('cryptocars', 'usd')
    token_ccar = token_ccar.get('cryptocars', 'usd')
    token_ccar_price = token_ccar.get('usd')
    token_brlccar_price = (float(token_ccar_price) * float(price_brl))
    token_ccar_text = f'${float(token_ccar_price):.6f} | R${float(token_brlccar_price):.2f}'

    embed = discord.Embed(title='')
    embed = embed.add_field(name='<:btc:905580814807478282> BTC:', value=token_btc_text)
    embed = embed.add_field(name='<:eth:905581264654958592> ETH:', value=token_eth_text)
    embed = embed.add_field(name='<:bnb:905581514367074324> BNB:', value=token_bnb_text)
    embed = embed.add_field(name='<:yel:905544368474165290> YEL:', value=token_yel_text)
    embed = embed.add_field(name='<:bfc:905580443108257862> BFC:', value=token_bfc_text)
    embed = embed.add_field(name='<:pvu:905546765330182194> PVU:', value=token_pvu_text)
    embed = embed.add_field(name='<:slp:905582281735954482> SLP:', value=token_slp_text)
    embed = embed.add_field(name='<:pmon:905582710058274816> PMON:', value=token_pmon_text)
    embed = embed.add_field(name='<:hero:905583274506723348> HERO:', value=token_metahero_text)
    embed = embed.add_field(name='<:cardano:905583427313602612> CARDANO:', value=token_cardano_text)
    embed = embed.add_field(name='<:MNSTRS:905583611410022410> MNSTRS:', value=token_mnstrs_text)
    embed = embed.add_field(name='<:dsbowl:905586282925801544> DOGE:', value=token_dsbowl_text)
    embed = embed.add_field(name='<:bnx:905584004718264410> BNX:', value=token_binaryx_text)
    embed = embed.add_field(name='<:bnx:905584004718264410> GOLD:', value=token_gold_text)
    embed = embed.add_field(name='<:mgpx:908143326191050842> MGPX:', value=token_mgpx_text)
    embed = embed.add_field(name='<:ccar:908147500911841300> CCAR:', value=token_ccar_text)
    embed = embed.add_field(name='EMPTY', value='EMPTY')

    embed = embed.set_footer(text=f'PancakeSwap & CoinGecko | {now}', icon_url=f'https://img1.gratispng.com/20180330/eje/kisspng-bitcoin-cryptocurrency-monero-initial-coin-offerin-bitcoin-5abdfe6b6c5365.2052061515224008754437.jpg')
    await ctx.send(embed=embed)

@client.command(name='symbol')
async def symbol(ctx, symbol, total='1'):
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
        await ctx.send(embed=token_embed_cg)

client.run(' maskared token =p ')