import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] < 2)
         {
            var x = 50 + 50 * v.P_LoopMain[playerID];

            trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", x, x);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, x);

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2) 
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 45, 3, 100);
            trg.Shape_Edge(playerID, 1, "60 + 1n Dragoon", 45, 3, 100);

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3) 
         {
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 100, 0);
            epic.Shape_Square(playerID, 1, "60 + 1n Archon", 50, 0);
            epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 0);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4) 
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 100, 100);
            epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 100);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 5) 
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }
         
         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         else if (v.P_LoopMain[playerID] == 6)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
      
         trg.SkillEnd();
      }
   }
}