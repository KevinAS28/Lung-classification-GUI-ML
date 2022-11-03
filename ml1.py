import torch
import torchvision
from PIL import Image
torch.manual_seed(0)

class_names = ['normal', 'covid','pneumonia','lung_opacity']

test_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(size=(224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def load_model():
    resnet18 = torchvision.models.resnet18()
    resnet18.fc = torch.nn.Linear(in_features=512, out_features=4)
    resnet18.load_state_dict(torch.load('checkpoint_Resnet18_ES_crossval4.pt', map_location=torch.device('cpu')))
    resnet18.eval()
    # resnet18.cuda()
    model = resnet18
    return model


class ChestXRayInferenceData(torch.utils.data.Dataset):
    def __init__(self, image_list, transform):
        # print('image_list: ', image_list)
        self.image_list = image_list
        self.transform = transform
    def __len__(self):
        return len(self.image_list)
    def __getitem__(self, index):
        image = Image.open(self.image_list[index]).convert('RGB')
        return self.transform(image), "unknown"

def inference(model, image_path):
    test_dataset = ChestXRayInferenceData([image_path], test_transform)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=False)
    images, labels = next(iter(test_loader))
    outputs = model(images)
    x, preds = torch.max(outputs, 1)
    return outputs, float(x), class_names[preds[0]]

