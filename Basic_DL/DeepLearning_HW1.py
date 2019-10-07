{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "# from sympy import *\n",
    "# from sympy import Symbol, solve\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0.],\n",
       "       [1., 1.],\n",
       "       [1., 2.],\n",
       "       [2., 1.]])"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = np.array([[0.0, 0.0], [1.0, 1.0], [1.0, 2.0], [2.0, 1.0]])\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-0.5, 3.0)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(data[:,0], data[:,1])\n",
    "plt.xlim(-0.5, 3.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "w2: -0.3246011561650831, w1: 2.2645973734753264, w0: 0.20191061548739722\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXoAAAD8CAYAAAB5Pm/hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvqOYd8AAAIABJREFUeJzt3Xl4VdWh/vHvAgIEAgmQQCAQwhjmMUAcKxbFolW00quoOBJtpVV7S1tqa2t7W1up/bW1+rtlUBwQtIpTFWlFLSIQSAgQYghDCAlJGJKQicwn6/6Rg0UMkJCT7DO8n+fJw+Fkn73f7CQvm3X2XttYaxEREf/VzukAIiLSulT0IiJ+TkUvIuLnVPQiIn5ORS8i4udU9CIifk5FLyLi51T0IiJ+TkUvIuLnOjix0fDwcBsTE+PEpkVEfFZycnKBtTaiua9zpOhjYmJISkpyYtMiIj7LGHPoQl6noRsRET+nohcR8XMqehERP6eiFxHxcyp6ERE/p6IXEfFzKnoRET/nsfPojTHtgSQg11p7nafWKyISiMqr68gqOMnBgpNkF1UwNir0gtflyQumHgLSge4eXKeIiN+qrnORVVDBwYJyDhZUfFHsBwtPcrys+kvL3n/54AvejkeK3hjTH7gW+A3wA0+sU0TEX9S66skqOMneo+VkHC1j39EyMo6WcaiwAle9/WK58JBODArvwvTYCGLCuzKoV1diwrsysFcXunTswE8vcPueOqL/E/AjoJuH1ici4pOKTtaQlldCWl4paXml7D1SRmZBObWuhkJvZyCmV1eG9QnhurF9GdI7hMHhIcSEd6Fb56BWydTiojfGXAccs9YmG2OuOMdyCUACQHR0dEs3KyLiKGstR0qrSMstZfepYs8tIa+k6otlosKCGRHZjekjehMbGcKw3t0Y2juEzkHt2zSrJ47oLwGuN8bMAjoD3Y0xL1trbz99IWvtEmAJQFxcnP3qakREvFdFTR27DpeQkl1MSvYJUnKKvxhHNwYGhXclLqYno/t1Z0xUKKP6dqdH144Op27Q4qK31i4CFgG4j+h/eGbJi4j4kvp6y8HCk/8p9exi9hwp5dRw+qDwrlw2NJyx/UMZGxXKyL7d6drJkcmAm8R7k4mItJE6Vz1peaUkHixk68EitmWdoKSyFoBunTowITqMBdOHMjG6B+MHhNHTS47Um8qjRW+t/QT4xJPrFBHxtJq6elJzi9mSWUTiwSKSs4o4WeMCGo7WrxkdyeSBPZgYHcaQiBDatTMOJ24ZHdGLiN9z1Vt2HS5m474CNmcWsj37BFW19QAM7xPCjZOimDaoF9MG9aR3984Op/U8Fb2I+KWcogo27DvOxn0FfLa/gNKqOoyBEZHduWVKNPGDezIlpie9Qjo5HbXVqehFxC+UVNay+UAhG/cf59N9BRwqrACgX2hnrhkTyWXDIrhkaLjPja97gopeRHyStZYDx8tZn36M9XuOkXzoBK56S9eO7Ykf3Iu7L47h0mERDInoijG+PcbeUip6EfEZ1XUuth4sYn36MT7ac4zsooaj9lF9u/Odrw3h8uERTBgQRscOmpj3dCp6EfFqBeXVfLynodg37D3OyRoXnTq045Kh4dz/tcFMj+1Nv7Bgp2N6NRW9iHid/JJKPth9hLW7j7AtqwhroU/3Tlw/IYoZI3tz8ZBwgju27TQCvkxFLyJeIbuwgrW781m7+wg7coqBhlMfv3flMK4e1YfR/boH/Fj7hVLRi4hj9h8rY21qw5H75/mlAIyJ6s7CmbFcMyaSIREhDif0Dyp6EWlTOUUVvLsrj3d25LHnSBkAk6LDeHTWSK4ZE8mAnl0cTuh/VPQi0uoKyqt5PzWft3fkkXzoBACTB/bgl98cxTVj+hIZ6n9Xo3oTFb2ItIqyqlr+mXaUt3fm8dn+Alz1lhGR3Vg4M5brx/fTkXsbUtGLiMfUuerZsO84byTn8mH6Uarr6okKC+b+ywdz/YR+jIjULaWdoKIXkRbbd7SM15MPsyYll+Nl1fTs2pFbpgzg+glRTIoO09kyDlPRi8gFKamo5d1defw9+TA7c4rp0M4wfURvbp7cn+mxvXV1qhdR0YtIk7nqLRv3F/B68mHWpR2hpq6eEZHd+Nm1I5k9MYrwAJgJ0hep6EXkvI6WVvHqthxe3ZZDbnElYV2CmDs1mpsn99eFTD5ARS8ijaqvt3y6v4CVWw6xfs8xXPWWy4aF8+i1I/n6yN506qApCHyFil5EvuR4WTWvJeWwels2OUWV9OrakfmXDebWqQMY2Kur0/HkAqjoRQRrLZsOFLIy8RD/TDtKXb3losG9+NHMEVw9uo+O3n2cil4kgJ2srmNNSi4vbMpi/7FywroEcdfFMdw6LVrzzPgRFb1IAMourODFzVm8mpRDWVUdY6NCeWrOeK4d15fOQTp69zcqepEAcWp45vnPsli/5yjtjeEbY/ty18UxuqjJz6noRfxcRU0db6bksuKzLPYdK6dX144smD6U26YN1GRiAUJFL+KnjpdV88KmLF7acoiSylpG9+vOH+aM5zoNzwQcFb2InzlwvJxln2byxvZcal31XD2qD/ddNpi4gT00PBOgVPQifsBaS9KhE/zt35l8mH6Ujh3acfPk/tx36SAG6+yZgKeiF/FhrnrLvz4/wt82ZJKSXUxYlyC+f+VQ5l0co3ln5AsqehEfVF3nYs32XP727wNkFVYQ3bMLv7phNDdP7k+Xjvq1li/TT4SID6mscbF6WzZLNmSSX1LF2KhQnpk7iWvGRNK+ncbfpXEtLnpjTGdgA9DJvb7XrbW/aOl6ReQ/yqvreGnzIZZvzKSgvIapMT35/bfGcdmwcL3BKufliSP6auBKa225MSYI2GiMWWut3eKBdYsEtOKKGp7/LIsVm7IoqazlsmHhLJg+lGmDezkdTXxIi4veWmuBcvdfg9wftqXrFQlkx8uqWb7xIC9tzuJkjYurRvVhwfShjB8Q5nQ08UEeGaM3xrQHkoGhwDPW2kRPrFck0BSWV/O3DZm8uDmL6rp6rhvXjwenD9FNtaVFPFL01loXMMEYEwa8aYwZY63dffoyxpgEIAEgOjraE5sV8RsnTtaw9NNMVmzKoqrWxewJUSy4cqjOgReP8OhZN9baYmPMJ8A1wO4zPrcEWAIQFxenoR0RoKSyluUbD/LcxoOcrKnjunH9eOjrwxjaWwUvnuOJs24igFp3yQcDM4DftziZiB8rq6rl+c+yWPppJmVVdcwaG8lDXx9ObGQ3p6OJH/LEEX1f4AX3OH074DVr7T88sF4Rv3Oyuo4XNmexZEMmxRW1XD2qDw/PGM6ofhqDl9bjibNudgETPZBFxG/V1NWzels2f1m/n4Lyaq4c0ZtHZgxnbP9Qp6NJANCVsSKtqL7e8u6uPJ76516yiyqYNqgnS+ZNZlJ0D6ejSQBR0Yu0AmstG/YV8OQHe0jLK2Vk3+48f/cUrhgeoStZpc2p6EU8bEdOMb9fu4fNmYUM6BnMn/5rAteP70c7zUUjDlHRi3jIgePl/GFdBmt3H6FX14788pujmDttIB07tHM6mgQ4Fb1ICxWdrOFPH+5lZWI2nTu04+EZw7jvssGEdNKvl3gH/SSKXKDqOhcvbMri6Y/2U1HjYu7UaB6aMUw3/BCvo6IXaSZrLe+nHuF3H6STU1TJlSN689NZIxjaWxc7iXdS0Ys0Q0r2Cf7nvXSSD51gRGQ3Xrp3KpcNi3A6lsg5qehFmuDwiQqe/CCDd3bmER7Sid/dNJY5cQN0VyfxCSp6kXOoqKnj2Y8PsOTTTAywYPpQHrhiiN5oFZ+in1aRRlhreXdXPk+8n05+SRU3TOjHj68ZQb+wYKejiTSbil7kDOn5pfzinTS2HixidL/uPH3rROJiejodS+SCqehF3Ioravjjv/by8pZDhAYH8Zsbx3DLlGiNw4vPU9FLwHPVW1Zvy+YP6zIoqazl9viB/OCq4YR16eh0NBGPUNFLQEvKKuIX76SRllfK1EE9efz60Yzsq7nhxb+o6CUgFZZX88TaPbyefJi+oZ15+taJXDeur2aWFL+kopeAUl9veS0ph999sIfyqjq+c8UQvnflULp01K+C+C/9dEvASM8v5dE3U9meXczUQT35n9ljGN5H0xaI/1PRi987WV3Hnz7cy3OfZREaHMQf5oznW5OiNEwjAUNFL37LWsu6tKM8/m4a+SVV3Dp1AD++ZoTOppGAo6IXv5RTVMEv3knjoz3HGBHZjb/OncTkgbpPqwQmFb34lTpXPSs2ZfHUP/fSzsDPrh3JXRfH0KG97vIkgUtFL37j87xSfrJmF7sOl/D1Eb359ewxmptGBBW9+IGqWhd/Wb+PJRsyCesSxF/nTuTasTonXuQUFb34tC2ZhSxak8rBgpPMmdyfR68dqTdbRc6gohefVFJZy+/W7mHV1myie3bh5XuncemwcKdjiXglFb34nA92H+Gxt3dTUF5NwuWDeWTGcII7tnc6lojXUtGLzygsr+axt9N4LzWfkX27s/zOKYztH+p0LBGvp6IXn/Dernx+/vZuyqpqWTgzloTLBxOkUyZFmkRFL16tsLyax95J471d+YyNCuUPc+KJjdT8NCLN0eKiN8YMAF4EIoF6YIm19s8tXa/I+6n5/Pyt3ZS6j+Lvv3ywLnwSuQCeOKKvA/7bWrvdGNMNSDbG/Mta+7kH1i0B6Myj+FfmxJOeX8rXFn9CXnEl/cKCWTgzltkTo5yOKuITWlz01tp8IN/9uMwYkw5EASp6aba1qfn8zH0U/8Orh3P/14bw3q58Fq1JpbLWBUBucSWL1qQCqOxFmsCjY/TGmBhgIpDoyfWK/yuuqOHnb6fx7s68L47iT43FL16X8UXJn1JZ62LxugwVvUgTeKzojTEhwBvAw9ba0kY+nwAkAERHR3tqs+IH/r33OD96fSeF5TX891XDeeCKIV86oyavuLLR153teRH5Mo8UvTEmiIaSX2mtXdPYMtbaJcASgLi4OOuJ7Ypvq6xx8cTadF7cfIhhvUNYfucUxkR99bz4fmHB5DZS6pqwTKRpWnwKg2mYOWo5kG6t/WPLI0kg2JlTzLV/+ZQXNx/i3ksH8e73Lm205AEWzowlOOjLV74GB7Vn4czYtogq4vM8cUR/CXAHkGqM2eF+7qfW2vc9sG7xM7Wuep75eD9Pf7SfPt068cp907h46LnnqDk1Dr94XYbOuhG5AJ4462YjoPlg5bwyj5fzyGs72ZlTzI0To/jl9aMJDQ5q0mtnT4xSsYtcIF0ZK63OWsvLWw7xm/fT6RzUnmfmTuLacX2djiUSMFT00qoKyqtZ+PedfJxxnMuHR7D45nH06d7Z6VgiAUVFL63m33uP89+v7aS0qpbHrx/NvIsG6q5PIg5Q0YvHVde5WPxBBss2HiS2TzdW3jdNE5GJOEhFLx61/1g531+Vwuf5pcy7aCA/nTWSzkG6KYiIk1T04hHWWlZvy+Hxd9MIDmrPsnlxzBjVx+lYIoKKXjyguKKGRWtSWbv7CJcM7cUfvz1Bb7iKeBEVvbTIlsxCHnl1B8fLqln0jRHMv2ww7drpDVcRb6Kilwviqrf89aP9/Hn9XqJ7dmHNdy9mXP8wp2OJSCNU9NJsx8qqeHj1DjYdKOTGiVH8evYYQjrpR0nEW+m3U5pl0/4Cvr96B2VVtTz5rXHMieuvc+NFvJyKXprEVW/58/p9PP3RPgaHd9W58SI+REUv53WstIqHVu9gc2YhN02K4tc3jKGrhmpEfIZ+W+WcNu4r4OFXUyivrmPxzeOYEzfA6Ugi0kwqemmUq97y5w/38vTH+xkaEcIr8+MZ3kdDNSK+SEUvX3GstIrvr05hS2YRcyb35/EbRtOlo35URHyVfnvlS7ZkFrLglRROVtfx1JzxfGtyf6cjiUgLqegFaJirZumnmfz+gwwG9urCK/OnaahGxE+o6IWyqloW/n0XH6Qd4RtjInny5nF069y0W/yJiPdT0Qe4vUfLeOClZA4VVfDorJHcd9kgXQAl4mdU9AHs7R25/OSNVLp26sDK+6YRP7iX05FEpBWo6ANQTV09v30/nRWbsogb2INnbpukaYVF/JiKPsDkl1Ty4MrtbM8u5p5LBrFo1giC2rdzOpaItCIVfQDZtL+A761KobLWxV/nTuS6cf2cjiQibUBFHwCstSzfeJDfvp/OoPCurL49nmE6dVIkYKjo/VxVrYtFa1J5MyWXmaP78NS3J2jueJEAo994P5ZbXMn9LyWxO7eUH1w1nAXTh+o2fyIBSEXvpxIzC/nuyu1U19WzdF4cV43q43QkEXGIit7PWGt5ecshHn/3c6J7dmHJvDiG9g5xOpaIOEhF70eq61w89lYaryblcOWI3vzplgl011QGIgHPI0VvjHkOuA44Zq0d44l1SvMcLa3igZeTSckuZsH0oTxy1XDaazxeRPDcEf0K4K/Aix5anzTD9uwTPPBSMuXVdTx72yRmje3rdCSPeysll8XrMsgrrqRfWDALZ8Yye2KU07EChva/b/NI0VtrNxhjYjyxLmme15Jy+Nmbu+kT2okX772YEZHdnY7kcW+l5LJoTSqVtS6g4WyiRWtSAVQ2bUD73/fp2ncf5aq3/Pb9dH70+i6mDurJuwsu9cuSB1i8LuOLkjmlstbF4nUZDiUKLNr/vq/N3ow1xiQACQDR0dFttVm/VFZVy8Ord7B+zzHuvGggP79uFB38eL6avOLKZj0vnqX97/varB2stUustXHW2riIiIi22qzfySmq4Ob/v5lP9h7n1zeM5vEbxvh1yQP0Cwtu1vPiWdr/vs+/G8LPbMsqYvYzn5FfUskLd0/ljotinI7UJhbOjCU4qP2XngsOas/CmbEOJQos2v++zyNFb4xZBWwGYo0xh40x93pivfIfrycf5raliXQPDuKtBy/h0mHhTkdqM7MnRvHETWOJCgvGAFFhwTxx01i9EdhGtP99n7HWtvlG4+LibFJSUptv1xe56i1PrtvD3/6dySVDe/Hs3MmEdtFFUCKByBiTbK2Na+7rdGWsFztZXcdDq3fwYfpRbo+P5hffHK2bhIhIs6novdThExXc90IS+46V86sbRjMvQMbjRcTzVPReKCX7BPNfTKK6rp4Vd0/hsmE6S0lELpyK3st8sDufh1bvoE/3zqxOmKKZJ0WkxVT0XsJay7JPD/LbtelMGBDGsnlx9Arp5HQsEfEDKnovUOeq55fvpvHylmyuHduXp749ns5nnLcsInKhVPQOO1ldx4JXtvNxxnEe+NoQfjQzVrf7ExGPUtE76EhJFfes2EbG0TJ+e+NY5k7THEAi4nkqeod8nlfKPSu2UVZVy/I747gitrfTkUTET6noHfBJxjEeXLmdbp2D+PsDFzOqn39OLywi3kFF38ZWJh7isbfTiO3TjefumkJkaGenI4mIn1PRt5H6esuT6zL4338fYHpsBE/PnURIJ+1+EWl9apo2UFNXz4/f2MWbKbnMnRbNr64f7fdzyIuI91DRt7Ly6jq+83Iyn+4r4IdXD+fB6UMxRqdPikjbUdG3omNlVdz9/Db2HClj8c3jmBM3wOlIIhKAVPStJPN4OfOe20pheQ3L7oxjuk6fFBGHqOhbQUr2Ce5ZsY12xrA6IZ7xA8KcjiQiAUxF72Hr04/y4Cvb6dO9My/cPZWY8K5ORxKRAKei96DVW7P56ZupjIkK5bm7phCu2SdFxAuo6D3AWstf1u/n/324l68Nj+DZ2ybRVefIi4iXUBu1UJ2rnp+/ncaqrdncPLk/T9w0Vvd1FRGvoqJvgapaFw+tTmFd2lEenD6EH14dq3PkRcTrqOgvUFlVLQkvJrM5s5BffHMUd18yyOlIIiKNUtFfgMLyau56fhvp+aX86b8mMHtilNORRETOSkXfTLnFldyxLJG8kkqWzotj+ghdCCUi3k1F3wz7jpZxx/KtnKyp46V7pzElpqfTkUREzktF30Q7coq56/mtBLVvx2v3X8TIvrpZiIj4BhV9E2zcV0DCS0mEh3TipXunMrCXrnYVEd+hoj+P91PzeWh1CkMiQnjxnqn07q47QomIb1HRn8PKxEP87K3dTI7uwfI7pxDaJcjpSCIizeaRSziNMdcYYzKMMfuNMT/xxDqd9uwn+3n0zd1cMTyCl+6dppIXEZ/V4iN6Y0x74BngKuAwsM0Y84619vOWrtsJ1loWr8vg2U8OcMOEfvxhzvgvpjR4KyWXxesyyCuupF9YMAtnxuocehHxep4YupkK7LfWZgIYY1YDNwA+V/T19ZZf/eNzVmzK4tap0fxm9hjatWuY0uCtlFwWrUmlstYFNJxPv2hNKoDKXkS8mieGbqKAnNP+ftj9nE9x1Vt+/MYuVmzK4r5LB/HbG/9T8gCL12V8UfKnVNa6WLwuo62jiog0iyeO6Bubxct+ZSFjEoAEgOjoaA9s1nNq6up55LUdvLcrn4e+PoyHZwz7yuRkecWVjb72bM+LiHgLTxzRHwZOv+t1fyDvzIWstUustXHW2riIiAgPbNYzqmpdfOflZN7blc9PZ43gkauGNzoDZb+w4EZff7bnRUS8hSeKfhswzBgzyBjTEbgFeMcD6211J6vruGfFNtbvOcavZ48h4fIhZ1124cxYgoPaf+m54KD2LJwZ29oxRURapMVDN9baOmPMAmAd0B54zlqb1uJkraykspa7n9/Kjpxinpoznm9N7n/O5U+94aqzbkTE1xhrvzKc3uri4uJsUlJSm2/3lMLyauY9t5W9R8v4yy0T+cbYvo5lERFpKmNMsrU2rrmvC7grY4+WVnHbskRyiipYMi+O6bGaZlhE/FtAFf3hExXMXZpIYXk1L9wzlfjBvZyOJCLS6gKm6LMLK7h16RbKqmp5+b5pTIzu4XQkEZE2ERBFf7DgJHOXbqGy1sUr8+MZExXqdCQRkTbj90V/4Hg5ty7ZQl295ZX74hnVTzcMEZHA4tdFv+9oGbcuTQQsq+bHExvZzelIIiJtzm+LPj2/lNuXJdKunWHV/HiG9lbJi0hg8sh89N4mLa+EuUu3ENS+Ha8mqORFJLD53RF96uESbl+eSNeO7VmVEK/7u4pIwPOrok/JPsG857YSGhzEqvnxDOjZxelIIiKO85uiTz5UxJ3PbaNn146sSognSrNKiogAflL0Ww8WcffzW+ndvTOr5scTGdrZ6UgiIl7D54t+68Ei7np+K31DG0q+d3eVvIjI6Xy66JOyTiv5hHh6d1PJi4icyWdPr2wYk99KpHu4RiUvItI4nyz67dknuPO5bQ1j8gkarhERORefK/odOcXcuXwr4SEdWTU/nj4qeRGRc/Kpot+ZU8wdyxPpGdJwCqXOrhEROT+fKfpdh4u5fXkiPbo0HMn3DdV58iIiTeETRb87t4TblyU2XPGaEE8/XQwlItJkXl/0u3NLuG1ZIt06N0xroCteRUSax6uL/vO8Um5fnkhIpw6sTtDcNSIiF8Jri37PkVJuW7aFLkHtNUGZiEgLeGXRHzhezu3LEunUoWGq4eheKnkRkQvldUWfXVjBbUsTAVg5f5rmkxcRaSGvmusmr7iSW5duoarOxeqEeIZEhDgdSUTE53nNEf2x0irmLt1CaVUtL987jRGR3Z2OJCLiF7yi6AvLq7ltWSLHy6p54Z6pjIkKdTqSiIjfcHzopqSiljuWbyXnRAUr7p7KpOgeTkcSEfErjh7Rl1XVMu/5rew/Vs6SO+KIH9zLyTgiIn6pRUVvjJljjEkzxtQbY+Ka89qKmjruWbGNtNwSnr1tEpcPj2hJFBEROYuWHtHvBm4CNjTnRdbC/BeTSD50gj/fMpEZo/q0MIaIiJxNi8borbXpAMaYZr3uUOFJig4U8tSc8Vw7rm9LIoiIyHm02Ri9MSbBGJNkjEkqq67jN7PHctOk/m21eRGRgHXeI3pjzIdAZCOfetRa+3ZTN2StXQIsAYgZMdbOnRbd5JAiInLhzlv01toZnt5oeEgnT69SRETOwisumBIRkdbT0tMrbzTGHAYuAt4zxqzzTCwREfGUlp518ybwpoeyiIhIK9DQjYiIn1PRi4j4ORW9iIifU9GLiPg5Fb2IiJ8z1tq236gxZUBGm2/Yc8KBAqdDtIAv5/fl7KD8TvP1/LHW2m7NfZFTNx7JsNY2a1pjb2KMSVJ+Z/hydlB+p/lD/gt5nYZuRET8nIpeRMTPOVX0Sxzarqcov3N8OTsov9MCMr8jb8aKiEjb0dCNiIifa5OiN8b0NMb8yxizz/1nj7Ms5zLG7HB/vNMW2c7FGHONMSbDGLPfGPOTRj7fyRjzqvvzicaYmLZP2bgmZL/LGHP8tP19nxM5z8YY85wx5pgxZvdZPm+MMX9xf327jDGT2jrj2TQh+xXGmJLT9v1jbZ3xXIwxA4wxHxtj0o0xacaYhxpZxpv3f1Pye+33wBjT2Riz1Riz053/8UaWaV73WGtb/QN4EviJ+/FPgN+fZbnytsjTxMztgQPAYKAjsBMYdcYy3wX+1/34FuBVp3M3I/tdwF+dznqOr+FyYBKw+yyfnwWsBQwQDyQ6nbkZ2a8A/uF0znPk7wtMcj/uBuxt5OfHm/d/U/J77ffAvU9D3I+DgEQg/oxlmtU9bTV0cwPwgvvxC8DsNtpuS0wF9ltrM621NcBqGr6O053+db0OfN00907praMp2b2atXYDUHSORW4AXrQNtgBhxhivuNN8E7J7NWttvrV2u/txGZAORJ2xmDfv/6bk91rufVru/muQ++PMN1Ob1T1tVfR9rLX50PBNAHqfZbnO7huIbzHGOP2PQRSQc9rfD/PVH5YvlrHW1gElQK82SXduTckO8C33f7tfN8YMaJtoHtPUr9FbXeT+r/laY8xop8OcjXtIYCINR5Wn84n9f4784MXfA2NMe2PMDuAY8C9r7Vn3f1O6x2NXxp7rJuLNWE20tTbPGDMY+MgYk2qtPeCZhM3W2L+OZ/6r2pRlnNCUXO8Cq6y11caYB2g4Oriy1ZN5jrfu+6bYDgy01pYbY2YBbwHDHM70FcaYEOAN4GFrbemZn27kJV61/8+T36u/B9ZaFzDBGBMGvGmMGWOtPf09n2btf48d0VtrZ1hrxzTy8TZw9NSXtc8LAAABy0lEQVR/69x/HjvLOvLcf2YCn9DwL7FTDgOnH+X2B/LOtowxpgMQinf8l/282a21hdbaavdflwKT2yibpzTl++OVrLWlp/5rbq19HwgyxoQ7HOtLjDFBNJTkSmvtmkYW8er9f778vvA9ALDWFtPQhdec8almdU9bDd28A9zpfnwn8PaZCxhjehhjOrkfhwOXAJ+3Ub7GbAOGGWMGGWM60vCGx5lnAp3+dd0MfGTd74447LzZzxhPvZ6GcUxf8g4wz332RzxQcmp40NsZYyJPjacaY6bS8HtY6Gyq/3BnWw6kW2v/eJbFvHb/NyW/N38PjDER7iN5jDHBwAxgzxmLNa972uhd5F7AemCf+8+e7ufjgGXuxxcDqTScIZIK3NsW2c6TexYN79gfAB51P/cr4Hr3487A34H9wFZgsNOZm5H9CSDNvb8/BkY4nfmM/KuAfKCWhqOXe4EHgAfcnzfAM+6vLxWIczpzM7IvOG3fbwEudjrzGfkvpWEYYBeww/0xy4f2f1Pye+33ABgHpLjz7wYecz9/wd2jK2NFRPycrowVEfFzKnoRET+nohcR8XMqehERP6eiFxHxcyp6ERE/p6IXEfFzKnoRET/3f63DkD78MIosAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "eta = 0.01\n",
    "init_w2 = random.uniform(0,1)\n",
    "init_w1 = random.uniform(0,1)\n",
    "init_w0 = random.uniform(0,1)\n",
    "\n",
    "w2_list = []\n",
    "w1_list = []\n",
    "w0_list = []\n",
    "\n",
    "for i in range(0, 1000): \n",
    "    for j in range(0, len(data)):\n",
    "        gradient_w2 = (-2)*(data[j,0]**2)*(data[j,1] - (init_w2 * data[j,0]**2 + init_w1 * data[j,0] + init_w0))\n",
    "        gradient_w1 = (-2)*data[j,0]*(data[j,1] - (init_w2 * data[j,0]**2 + init_w1 * data[j,0] + init_w0))\n",
    "        gradient_w0 = (-2)*(data[j,1] - (init_w2 * data[j,0]**2 + init_w1 * data[j,0] + init_w0))\n",
    "                            \n",
    "        w2_list.append(gradient_w2)\n",
    "        w1_list.append(gradient_w1)\n",
    "        w0_list.append(gradient_w0)\n",
    "     \n",
    "        gradient_w2 = sum(w2_list)\n",
    "        gradient_w1 = sum(w1_list)\n",
    "        gradient_w0 = sum(w0_list)\n",
    "        \n",
    "        w2_next = init_w2 - eta*gradient_w2; init_w2 = w2_next\n",
    "        w1_next = init_w1 - eta*gradient_w1; init_w1 = w1_next\n",
    "        w0_next = init_w0 - eta*gradient_w0; init_w0 = w0_next\n",
    "        \n",
    "    if i < 49: \n",
    "        continue\n",
    "        \n",
    "    else:\n",
    "        final_w2 = w2_next\n",
    "        final_w1 = w1_next\n",
    "        final_w0 = w0_next\n",
    "        \n",
    "print('w2: {0}, w1: {1}, w0: {2}'.format(final_w2, final_w1, final_w0))\n",
    "\n",
    "x = np.arange(-0.5, 3.0, 0.01)\n",
    "y = final_w2*(x**2) + final_w1*x + final_w0\n",
    "\n",
    "plt.scatter(data[:,0], data[:,1])\n",
    "plt.xlim(-0.5, 3.0)\n",
    "plt.plot(x, y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "godsw",
   "language": "python",
   "name": "godsw"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
