import numpy as np

class ZMeans:
  '''
  ZMeans color space clustering
  Lab: euclidean metric
  RGB: color metric
  '''

  n_clusters = 3
  max_iter = 100
  tol = 1e-3

  metric = "color"
  init = "random"

  verbose = 0

  trace_ = []
  inertia_ = []

  data_ = None
  centers_ = None
  labels_ = None
  metrics_ = None

  def __init__(self,n_clusters=3,max_iter=100,tol=1e-3,metric="color",verbose=0):
    '''Init by n_clusters, max_iter: max. iterations, tol: tolerance, metric: color, euclidean'''
    super().__init__()
    self.n_clusters = n_clusters
    self.max_iter = max_iter
    self.tol = tol
    self.metric = metric
    self.verbose = verbose

  def check_params_():
    pass
  
  def init_(self):
    '''init interal structures'''
    c_min,c_max = self.data_.min(axis=0), self.data_.max(axis=0)    
        
    self.centers_ = np.linspace(c_min,c_max,num=self.n_clusters)
    
    self.metrics_ = np.zeros((self.data_.shape[0],self.n_clusters))
    self.inertia_ = []
    self.trace_ = []
    
  def fit(self,data):
    '''fit data'''

    self.data_ = data.copy()
    self.init_()

    if (0!=self.verbose): print(self.metric,self.n_clusters,self.max_iter)

    for it in range(self.max_iter):

      for k in range(self.n_clusters): 
        self.metrics_[:,k] = ZMeans.compute_metric(self.data_,self.centers_[k,:],metric=self.metric)

      self.labels_ = np.argmin(self.metrics_,axis=1)
      self.inertia_.append(np.min(self.metrics_,axis=1).sum())
      self.trace_.append(self.centers_.copy())
      
      self.centers_,tol = ZMeans.compute_centers(self.data_,self.labels_,self.trace_[-1],self.metric)

      if (0!=self.verbose): print(it,tol)
      if np.abs(tol) <= self.tol: break

    return self

  @staticmethod
  def compute_centers(data,labels,trace,metric):
    '''centers by data, labels, metric'''    
    n_clusters = trace.shape[0]
    centers = trace.copy()
    tol = 0
    for k in range(n_clusters):
      ii = np.argwhere(labels==k)      
      if len(ii)>0: centers[k,:] = data[ii,].mean(axis=0)
      tol = tol + ZMeans.compute_metric(trace[k,:],centers[k,:],metric=metric)
    return centers,tol

  @staticmethod
  def compute_metric(X,p,metric="color"):
    '''metrics by X, p: center and given metric (default: color)'''
    if len(X.shape) == 1: X = X[np.newaxis,]
    if "euclidean"==metric:
      return np.sqrt(np.sum((X-p)**2,axis=1))     
    if "color"==metric:
      # rgb -> cixyz -> cilab
      rm = (X[:,0]+p[0])/2.
      X2 = (X-p)**2
      r,g,b = (2.+rm)*X2[:,0],4.*X2[:,1],(3.-rm)*X2[:,2]
      return np.sqrt(np.abs(np.sum(np.array([r,g,b]).T,axis=1)))
    return np.NaN
  
  @staticmethod
  def score_partition(labels):    
    '''compute partition score'''
    rc = np.unique(labels,return_counts=True)
    return rc[0],rc[1].astype(np.float64)/len(labels)
  
import cv2

class ZMeansUtils:
  '''utility interface'''

  @staticmethod  
  def image_(fname):
    '''load image by filename, return Lab, BGR, RGB'''
    bgr = cv2.imread(fname)
    # convert BGR to uniform LAB space
    lab = cv2.cvtColor(bgr.copy(),cv2.COLOR_BGR2LAB)    
    rgb = cv2.cvtColor(bgr.copy(),cv2.COLOR_BGR2RGB)    
    return lab,bgr,rgb

  @staticmethod  
  def cluster_(data,k,metric):
    '''cluster data with k clusters by metric, return centers and labels'''  
    engine = ZMeans(n_clusters=k,metric=metric,verbose=0).fit(data)    
    return engine.centers_.copy(), engine.labels_.copy()

  @staticmethod  
  def mask_(image,centroid,labels,mode="min"): 
      '''prepare an image mask by min. or max. mode, return band, mask and zoom'''
      mask = np.zeros(image.shape[:2]).reshape(-1,1)
      if "min"==mode:
        label = np.argmin(np.mean(centroid,axis=1))
        mask[np.where(labels!=label)] = 1    
      else: 
        label = np.argmax(np.mean(centroid,axis=1))
        mask[np.where(labels==label)] = 1          
      mask = mask.reshape(image.shape[:2])
      nw = np.where(mask>0)
      zoom = (nw[0].min(),nw[0].max(),nw[1].min(),nw[1].max())
      band = cv2.bitwise_and(image,image,mask=mask.astype(np.uint8))
      return band,mask,zoom
  
  @staticmethod
  def zoom_(images,zoom):
    '''zoom images array to zoom xy-range'''
    return [image[zoom[0]:zoom[1],zoom[2]:zoom[3],:].astype(np.float32)/255. for image in images]
  
  @staticmethod
  def colormap_(image,centers,labels,cmap):
    '''map image to colors of cmap for k labels'''
    image_ = image.reshape(-1,3)
    for k in np.unique(labels):
        image_[np.argwhere(image_==centers[k,].astype(np.float32)),] = np.array(cmap(k)[:3])*255.
    return image_.reshape(image.shape)
  
  @staticmethod
  def partition_(images):
    '''partition images'''
    rc = []
    for image in images:
      image_ = image.reshape(-1,image.shape[-1])
      tuples_ = [tuple(image_[j,]) for j in range(image_.shape[0])]
      label_,partition_ = np.unique(tuples_,axis=0,return_counts=True)
      #partition_ = partition_/np.sum(partition_)
      rc.append([label_,partition_])
    return rc
# -----------------------------

def test_():

  import cv2
  import os
  
  os.system('cls')

  fpath = os.path.join(os.getcwd(),"data")
  fname = "SMA_20230207_130757327.jpg"

  I = cv2.imread(os.path.join(fpath,fname))
  I = cv2.cvtColor(I,cv2.COLOR_BGR2RGB)
          
  X = I.reshape(-1,3)
  
  n_clusters = 3

  for metric in ["euclidean","color"]:

    engine = ZMeans(
      n_clusters=n_clusters,
      verbose=1,
      metric=metric,
      max_iter=100
      ).fit(X)

    print(engine.centers_)
    print(ZMeans.score_partition(engine.labels_))


if __name__=="__main__":
  test_()
