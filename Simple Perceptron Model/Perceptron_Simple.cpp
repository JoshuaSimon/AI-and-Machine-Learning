// Perceptron_Simple.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

#include <iostream>
#include <vector>
using namespace std;

class perceptron
{
public:
	perceptron(float eta, int epochs);
	float netInput(vector<float> X);
	int predict(vector<float> X);
	void fit(vector< vector<float> > X, vector<float> y);
	void printErrors();
	void printWeights();
private:
	float m_eta;
	int m_epochs;
	vector < float > m_w;
	vector < float > m_errors;
};

perceptron::perceptron(float eta, int epochs)
{
	m_epochs = epochs; 
	m_eta = eta; 
}

int perceptron::predict(vector<float> X)
{
	return netInput(X) > 0 ? 1 : -1; //Step Function
}

float perceptron::netInput(vector<float> X)
{
	// Sum(Vector of weights * Input vector) + bias
	float probabilities = m_w[0];
	for (int i = 0; i < X.size(); i++)
	{
		probabilities += X[i] * m_w[i + 1];
	}
	return probabilities;
}

void perceptron::fit(vector< vector<float> > X, vector<float> y)
{
	for (int i = 0; i < X[0].size() + 1; i++) // X[0].size() + 1 -> +1 to add the bias term
	{
		float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
		m_w.push_back(r);
	}

	for (int i = 0; i < m_epochs; i++)
	{
		int errors = 0;
		for (int j = 0; j < X.size(); j++)
		{
			float update = m_eta * (y[j] - predict(X[j]));
			for (int w = 1; w < m_w.size(); w++) { m_w[w] += update * X[j][w - 1]; }
			m_w[0] = update;
			errors += update != 0 ? 1 : 0;
		}
		m_errors.push_back(errors);
	}
}


void perceptron::printErrors()
{
	cout << "errors: ";
	for (int i = 0; i < m_errors.size(); i++)
	{
		cout << m_errors[i] << " ";
	}
	cout << endl;
}


void perceptron::printWeights()
{
	cout << "weights: ";
	for (int i = 0; i < m_w.size(); i++)
	{
		cout << m_w[i] << " ";
	}
	cout << endl;
}



int main() {
	// input vectors - first element is bias neuron
	/*vector <vector <float>> X = {
		{1, 0, 0},
		{1, 0, 1},
		{1, 1, 0},
		{1, 1, 1}
	};*/
	
	vector <vector<float> > X = {
		{0, 0},
		{0, 1},
		{1, 0},
		{1, 1}
	};

	// Outputs
	vector<float> y = { 0,1,1,1 };

	perceptron p(0.1, 500);
	p.fit(X, y);
	p.printErrors();
	p.printWeights();
	

	system("Pause");
}


