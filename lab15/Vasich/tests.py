from lab15.Vasich.lca_to_rmq import LCATree
from random import shuffle, randint
import unittest


class TestLCA(unittest.TestCase):

    def test_root_only(self):
        t = LCATree("root", 1)
        t.prepare()
        self.assertEqual(t.find_lca("root", 2), "Missing keys:\tv2 = 2")

    def test_human_evolution(self):
        aust_afar = "Australopithecus Afarensis"
        aust_afri = "Australopithecus Africanus"

        para_aeth = "Paranthropus Aethiopicus"
        para_robu = "Paranthropus Robustus"
        para_bois = "Paranthropus Boisei"

        homo_rudo = "Homo Rudolfensis"
        homo_habi = "Homo Habilis"
        homo_erga = "Homo Ergaster"
        homo_erec = "Homo Erectus"
        homo_heid = "Homo Heidelbergensis"
        homo_nean = "Homo Neanderthalensis"
        homo_sapi = "Homo Sapiens"

        t = LCATree(aust_afar, 12)
        t.add_link(aust_afar, para_aeth)
        t.add_link(para_aeth, para_robu)
        t.add_link(para_aeth, para_bois)
        t.add_link(aust_afar, aust_afri)
        t.add_link(aust_afri, homo_rudo)
        t.add_link(aust_afri, homo_habi)
        t.add_link(homo_habi, homo_erga)
        t.add_link(homo_erga, homo_erec)
        t.add_link(homo_erga, homo_heid)
        t.add_link(homo_heid, homo_nean)
        t.add_link(homo_heid, homo_sapi)

        t.prepare()

        self.assertEqual(t.find_lca(homo_heid, homo_rudo), aust_afri)
        self.assertEqual(t.find_lca(homo_sapi, homo_erec), homo_erga)
        self.assertEqual(t.find_lca(para_aeth, homo_habi), aust_afar)
        self.assertEqual(t.find_lca("Gorilla beringei", homo_erec), "Missing keys:\tv1 = Gorilla beringei")

    def test_random_order(self):
        t = LCATree(3, 8)
        links = [(1, 7), (4, 7), (7, 3), (5, 3), (2, 5), (6, 2), (8, 2)]
        shuffle(links)

        for link in links:
            i = randint(0, 1)
            t.add_link(link[i], link[1 - i])

        t.prepare()

        self.assertEqual(t.find_lca(1, 8), 3)
        self.assertEqual(t.find_lca(6, 2), 2)
        self.assertEqual(t.find_lca(2, 6), 2)
        self.assertEqual(t.find_lca(1, 4), 7)
