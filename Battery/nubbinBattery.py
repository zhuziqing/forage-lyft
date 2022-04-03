from battery.battery import Battery

class NubbinBattery(Battery):
   def _init_(self, lastServiceDate, currentDate){
      self.currentDate = currentDate
      self.lastServiceDate = lastServiceDate

   def needs_service(self):
      nextServiceDate = self.calculateDate(self.lastServiceDate,4)
      if nextServiceDate < self.currentDate:
           return True
      else:
           return False

   def calculateDate(dateToBeAdded, years):
      result = dateToBeAdded.replace(year = dateToBeAdded.year + years)
      return result
