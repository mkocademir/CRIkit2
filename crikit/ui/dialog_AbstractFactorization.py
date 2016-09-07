# -*- coding: utf-8 -*-
"""
Abstract Factorization Class

Created on Mon Jul 25 10:44:03 2016

@author: chc
"""

import sys as _sys
import numpy as _np

from PyQt5 import QtWidgets as _QtWidgets
from PyQt5.QtWidgets import (QApplication as _QApplication,
                             QDialog as _QDialog)
import PyQt5.QtCore as _QtCore

# Import from Designer-based GUI
from crikit.ui.qt_Factorization import Ui_Dialog ### EDIT ###

# Generic imports for MPL-incorporation
import matplotlib as _mpl

from sciplot.ui.widget_mpl import MplCanvas as _MplCanvas

_mpl.use('Qt5Agg')
_mpl.rcParams['font.family'] = 'sans-serif'
_mpl.rcParams['font.size'] = 12

class DialogAbstractFactorization(_QDialog):
    """
    SubUiSVD : SVD SubUI
    """

    def __init__(self, data, img_shape, parent=None):
#        raise NotImplementedError('This is an abstract class.')
        super(DialogAbstractFactorization, self).__init__(parent) ### EDIT ###
        self.setup()
        self.setupData(img_shape=img_shape)
        self.ui_changes()
#        pass

        
    def ui_changes(self):
        """
        Any changes to ui labels or otherwise for particular implementation
        """
        pass
    
    def setupData(self, img_shape):
        self._img_shape = img_shape
        self._n_y = img_shape[0]
        self._n_x = img_shape[1]
        self._n_spectra = img_shape[2]
        self._n_factors = None

        self.selected_factors = set()
        
    def setup(self, parent = None):

        # Generic load/init designer-based GUI
        super(DialogAbstractFactorization, self).__init__(parent) ### EDIT ###

        self.ui = Ui_Dialog() ### EDIT ###
        self.ui.setupUi(self)     ### EDIT ###

        self.ui.pushButtonNext.clicked.connect(self.advance)
        self.ui.pushButtonPrev.clicked.connect(self.advance)
        self.ui.pushButtonGoTo.clicked.connect(self.advance)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonClear.clicked.connect(self.clear)
        self.ui.pushButtonApply.clicked.connect(self.applyCheckBoxes)
        self.ui.pushButtonScript.clicked.connect(self.runScript)

        self._first_factor_visible = 0
        self._num_factor_visible = 6

        self.ui.lcdSelectedFactors.display(0)

        self.factorWins = []
        self.factorLabelCheckBoxes = [self.ui.checkBox,
                                  self.ui.checkBox_2,
                                  self.ui.checkBox_3,
                                  self.ui.checkBox_4,
                                  self.ui.checkBox_5,
                                  self.ui.checkBox_6]

        for count in range(self._num_factor_visible):
            self.factorWins.append(_MplCanvas(subplot=211))
            self.factorWins[count].ax[0].axis('Off')
            self.factorWins[count].ax[1].hold('Off')

        self.ui.gridLayout.addWidget(self.factorWins[0],1,0)
        self.ui.gridLayout.addWidget(self.factorWins[1],1,1)
        self.ui.gridLayout.addWidget(self.factorWins[2],1,2)

        self.ui.gridLayout.addWidget(self.factorWins[3],3,0)
        self.ui.gridLayout.addWidget(self.factorWins[4],3,1)
        self.ui.gridLayout.addWidget(self.factorWins[5],3,2)

        self.reconCurrent = _MplCanvas(subplot=211)
        self.reconCurrent.ax[0].axis('Off')
        self.reconCurrent.ax[1].hold('Off')

        self.reconRemainder = _MplCanvas(subplot=211)
        self.reconRemainder.ax[0].axis('Off')
        self.reconRemainder.ax[1].hold('Off')


        self.ui.verticalLayout_3.insertWidget(1,self.reconCurrent)
        self.ui.verticalLayout_3.insertWidget(4,self.reconRemainder)

        for count in range(self._num_factor_visible):
            self.factorLabelCheckBoxes[count].setText('Keep: ' + str(count))

    @property
    def unselected_factors(self):
        all_factors = set(_np.arange(self._n_factors))
        return all_factors - self.selected_factors
        
    @classmethod
    def main(cls, data, img_shape, parent=None):
        """
            Executes DialogAbstractFactorization dialog and returns values
        """
#        raise NotImplementedError
        
        dialog = cls(data, img_shape, parent)
        dialog.showMaximized()
        result = dialog.exec_()  # 1 = Aceepted, 0 = Rejected/Canceled

        if result == 1:
            factors = list(dialog.selected_factors)
            if len(factors) == 0:
                factors = None
            else:
                factors.sort()
                factors = _np.array(factors)
            return factors
        else:
            return None

    def applyCheckBoxes(self):
        """
        Add checked singular values (and remove un-checked SVs)
        """
        for count, checkBox in enumerate(self.factorLabelCheckBoxes):
            if checkBox.isChecked() == True:
                self.selected_factors.add(self._first_factor_visible+count)
            else:
                try:
                    self.selected_factors.remove(self._first_factor_visible+count)
                except:
                    pass

        #print('Self.S: {}'.format(self.svddata.S[0:3]))
        self.ui.lcdSelectedFactors.display(len(self.selected_factors))
        self.updateCurrentRemainder()

    def advance(self):
        """
        View next set of SVs
        """
        sender = self.sender().objectName()
        if sender == 'pushButtonPrev':
            self.updatePlots(startnum=self._first_factor_visible-self._num_factor_visible)
        elif sender == 'pushButtonNext':
            self.updatePlots(startnum=self._first_factor_visible+self._num_factor_visible)
        elif sender == 'pushButtonGoTo':
            self.updatePlots(startnum=self.ui.spinBoxGoTo.value())
        else:
            pass
    def runScript(self):
        """
        Run "script" of singular value selection

        Example:
            [1,2,3,5:7] = 1,2,3,5,6,7
        """
        script = self.ui.lineEditSelections.text()
        script = script.strip('[').strip(']')
        script = script.split(',')
        for count in script:
            if ':' in count:
                temp = count.split(':')
                self.selected_factors.update(set(_np.arange(int(temp[0]),int(temp[1])+1)))
            elif count.strip() == '':
                pass
            else:
                self.selected_factors.add(int(count))
        self.updatePlots(startnum=self._first_factor_visible)
        self.ui.lcdSelectedFactors.display(len(self.selected_factors))
        self.updateCurrentRemainder()

    def combiner(self, factors=None):
        raise NotImplementedError('combiner method not implemented')

    def mean_spatial(self, cube):
        raise NotImplementedError('mean_spatial method not implemented')
        
    def mean_spectral(self, cube):
        raise NotImplementedError('mean_spectral method not implemented')
               
    def get_spatial_slice(self, num):
        raise NotImplementedError('get_spatial_slice method not implemented.')
        
    def get_spectral_slice(self, num):
        raise NotImplementedError('get_spectral_slice method not implemented.')
        
    def updateCurrentRemainder(self):
        """
        Update image reconstructed (mean over spectral vector) using remaining \
        (unselected) singular values
        """
        cube_select = self.combiner(self.selected_factors)
        img_select = self.mean_spatial(cube_select)
        spect_select = self.mean_spectral(cube_select)
        
        cube_nonselect = self.combiner(self.unselected_factors)
        img_nonselect = self.mean_spatial(cube_nonselect)
        spect_nonselect = self.mean_spectral(cube_nonselect)
        
        self.reconCurrent.ax[0].cla()
        self.reconCurrent.ax[1].cla()
        
        self.reconCurrent.ax[0].imshow(img_select, interpolation='None', 
                                       cmap = _mpl.cm.gray, origin='lower')
        self.reconCurrent.ax[1].plot(spect_select)
        self.reconCurrent.draw()
        
        self.reconRemainder.ax[0].cla()
        self.reconRemainder.ax[1].cla()
        self.reconRemainder.ax[0].imshow(img_nonselect, interpolation='None', 
                                       cmap = _mpl.cm.gray, origin='lower')
        self.reconRemainder.ax[1].plot(spect_nonselect)
        self.reconRemainder.draw()
                

    def updatePlots(self, startnum=0):
        """
        Update images and spectra of set of singular values starting at SV \
        number startnum
        """
        if startnum <= 0:
            startnum = 0
            self.ui.pushButtonPrev.setEnabled(False)
            self.ui.pushButtonNext.setEnabled(True)
        elif startnum > self._n_factors - self._num_factor_visible:
            startnum = self._n_factors - self._num_factor_visible
            self.ui.pushButtonPrev.setEnabled(True)
            self.ui.pushButtonNext.setEnabled(False)
        else:
            self.ui.pushButtonPrev.setEnabled(True)
            self.ui.pushButtonNext.setEnabled(True)

        self._first_factor_visible = startnum

        for count in range(self._num_factor_visible):
            self.factorWins[count].ax[0].clear()

            self.factorWins[count].ax[0].imshow(self.get_spatial_slice(count 
                + self._first_factor_visible), interpolation='none',
                cmap = _mpl.cm.gray , origin='lower')

            self.factorWins[count].ax[0].axis('Off')

            self.factorWins[count].ax[1].clear()
            self.factorWins[count].ax[1].plot(self.get_spectral_slice(count + self._first_factor_visible))

            self.factorLabelCheckBoxes[count].setText('Keep: ' + str(startnum + count))
            self.factorWins[count].draw()
            if self._first_factor_visible + count in self.selected_factors:
                self.factorLabelCheckBoxes[count].setChecked(True)
            else:
                self.factorLabelCheckBoxes[count].setChecked(False)

    def clear(self):
        """
        Clear selected singular values (i.e., none will be selected)
        """
        self.selected_factors = set()
        self.ui.lcdSelectedFactors.display(len(self.selected_factors))
        self.updateCurrentRemainder()
        self.updatePlots(startnum=self._first_factor_visible)


if __name__ == '__main__':
    app = _QApplication(_sys.argv)
    app.setStyle('Cleanlooks')
    x = _np.linspace(100,200,50)
    y = _np.linspace(200,300,50)
    f = _np.linspace(500,3000,800)
    Ex = 30*_np.exp((-(f-1750)**2/(200**2)))
    Spectrum = _np.convolve(_np.flipud(Ex),Ex,mode='same')

    data = _np.zeros((y.size,x.size,f.size))

    for count in range(y.size):
        data[count,:,:] = y[count]*_np.random.poisson(_np.dot(x[:,None],Spectrum[None,:]))

    win = DialogAbstractFactorization.main(None, DialogAbstractFactorization) ### EDIT ###

    print(win)


    _sys.exit(app.exec_())
#    _sys.exit()