import variable as v;
import func.trig as trg;
import func.trigadv as adv;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 7)
         {
            trg.Table_Sin(playerID, 30 + 30 * v.P_LoopMain[playerID], 125);
            trg.Table_Cos(playerID, 30 + 30 * v.P_LoopMain[playerID], 125);
            
            var x = v.P_AngleCos[playerID];
            var y = v.P_AngleSin[playerID];

            adv.Shape_QuadNxNSquareAt(playerID, 1, "50 + 1n Battlecruiser", 2, 50, x, y);
            trg.Shape_Square(playerID, 1, "40 + 1n Goliath", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         }

         trg.Main_Wait(240);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 12)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 4, 100);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 3)
         {
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);

            trg.Shape_Edge(playerID, 1, " Creep. Dunkelheit", 0, 4, 100);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 6)
         {
            var x = 100;
            var y = 0;

            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 2, 50, x, y);
            trg.Shape_Square(playerID, 2, "40 + 1n Ghost", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);

            var x = 100;
            var y = 100;

            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 2, 50, x, y);
            trg.Shape_Square(playerID, 2, "40 + 1n Ghost", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 10)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {      
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}