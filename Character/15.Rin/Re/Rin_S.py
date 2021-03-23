import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 2)
         {          
            var d = 0;
            var n = 8; 
            var r = 75 + 75 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "60 + 1n High Templar", d, n, r);
            epic.Shape_Circle(playerID, 1, "60 + 1n Danimoth", d, n, r, 1);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }

         trg.Main_Wait(320);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 2)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {      
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         trg.SkillEnd();
      }
   }
}