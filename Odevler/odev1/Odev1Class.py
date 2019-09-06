#Created by utkuglsvn
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class DataClass:
    def __init__(self):
        self.anakitle = np.random.randint(0, 100, 10000)
        np.random.seed(15)
        self.orneklem = np.random.choice(a=self.anakitle, size=15)
        print("orneklem:",self.orneklem)

    def ortalama(self):
        print("orneklem ortalama:",self.orneklem.mean())

    def pdf_ciz(self):
        veri_normal = norm.rvs(size=10000, loc=0, scale=1)
        ax = sns.distplot(veri_normal)
        # ax=sns.distplot(veri_normal,bin())
        ax.set(xlabel='Normal', ylabel='Frekans')
        plt.title("pdf grafigi")
        plt.show()

    def cdf_ciz(self):# kümalatif dagılım fonk
        x = np.random.randn(10000)
        norm_cdf = norm.cdf(x)
        sns.lineplot(x=x, y=norm_cdf)
        plt.title("cdf grafigi")
        plt.show()

    def cizgi_grafigi_ciz(self):
        x = [2, 4, 6]
        y = [1, 3, 5]
        plt.plot(x, y)
        plt.title("cizgi grafigi")
        plt.show()

    def histogram_ciz(self):
        number_of_samples = 10000
        np.random.seed(42)
        y = np.random.randn(number_of_samples)
        plt.hist(y, bins=100);
        plt.title("histogram grafigi")
        plt.show()

    def dagilim_grafigi_ciz(self):
        iris = load_iris()
        plt.scatter(iris.data[:, 0], iris.data[:, 1])
        plt.xlabel(iris.feature_names[0])
        plt.ylabel(iris.feature_names[1])
        plt.title("dagilim grafgi")
        plt.show();

a=DataClass()
a.ortalama()
a.pdf_ciz()
a.cdf_ciz()
a.cizgi_grafigi_ciz()
a.histogram_ciz()
a.dagilim_grafigi_ciz()