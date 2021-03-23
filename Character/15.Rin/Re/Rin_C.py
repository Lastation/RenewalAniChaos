import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 3)
         {          
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 50, 50);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 50, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 75, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 75, 0);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order( "40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All,  "40 + 1n Mojo", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 50);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 50, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order( "40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All,  "40 + 1n Mojo", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 5)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 50, 0);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order( "40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All,  "40 + 1n Mojo", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 6)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {      
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         trg.SkillEnd();
      }
   }
}