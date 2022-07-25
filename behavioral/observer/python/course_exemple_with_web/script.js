class Observable {
   subscribe(observer) {};
   unsubscribe(observer) {};
   notify() {};
}

class Observer {
   update() {};
}

class ObservableInput extends Observable {
   observers = [];

   constructor(element) {
      super();
      this.element = element;
   }

   subscribe(...observers) {
      observers.forEach(observer => {
         if (! this.observers.includes(observer)) {
            this.observers.push(observer);
         }
      });
      
   }

   unsubscribe(observer) {
      observerIndex = this.observers.indexOf(observer);
      if (observerIndex === -1) return;
      this.observers.splice(observerIndex, 1);
   }

   notify(observer) {
      this.observers.forEach(observer => observer.update(this));
   }
   
}

class ObserverParagraph extends Observer {
   constructor(element) {
      super();
      this.element = element;
   }

   update(observable) {
      this.element.innerHTML = observable.element.value;
   }
}

class ObserverDiv extends Observer {
   constructor(element) {
      super();
      this.element = element;
   }

   update(observable) {
      this.element.innerHTML = observable.element.value;
   }
}



function makeInput() {
   const input = document.createElement('input');
   document.body.appendChild(input);
   return input;
}

function makeParagraph() {
   const p = document.createElement('p');
   document.body.appendChild(p);
   p.innerText = 'Initial HardCoded Text To Paragraph'
   return p;
}

function makeDiv() {
   const div = document.createElement('div');
   document.body.appendChild(div);
   div.innerText = 'Initial HardCoded Text To Div'
   return div;
}

input = new ObservableInput(makeInput());
paragraph = new ObserverParagraph(makeParagraph());
div = new ObserverDiv(makeDiv());

input.subscribe(paragraph, div);
input.subscribe(paragraph, div);
input.element.addEventListener('keyup', function(){
   input.notify(this)
});


