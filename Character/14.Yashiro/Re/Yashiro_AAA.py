import variable as v;
import func.trig as trg;
import func.trigadv as adv;

function main(playerID)
{

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.ComputerAlly(1);
            SetInvincibility(Enable, v.P_UnitID[playerID], playerID, "Anywhere");

            trg.Table_Sin(playerID, 0, 150);
            trg.Table_Cos(playerID, 0, 150);
            
            var x = v.P_AngleCos[playerID];
            var y = v.P_AngleSin[playerID];

            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Ghost", 4, 32, x, y);
            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Guardian", 3, 50, x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {          
            trg.Table_Sin(playerID, 0, 150);
            trg.Table_Cos(playerID, 0, 150);
            
            var x = v.P_AngleCos[playerID];
            var y = v.P_AngleSin[playerID];

            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 3, 50, x, y);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {          
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);

            trg.Table_Sin(playerID, 45, 225);
            trg.Table_Cos(playerID, 45, 225);
            
            var x = v.P_AngleCos[playerID];
            var y = v.P_AngleSin[playerID];

            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Ghost", 4, 32, x, y);
            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Guardian", 3, 50, x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {          
            trg.Table_Sin(playerID, 45, 225);
            trg.Table_Cos(playerID, 45, 225);
            
            var x = v.P_AngleCos[playerID];
            var y = v.P_AngleSin[playerID];

            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 3, 50, x, y);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         else if (v.P_LoopMain[playerID] == 4)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 10)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 4)
         {         
            RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", playerID);

            var d = 90 / 4 * v.P_LoopMain[playerID];
            var n = 3; 
            var r = 100;
            trg.Shape_Circle(playerID, 16, "80 + 1n Vulture", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("80 + 1n Vulture", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 8)
         {
            RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", playerID);

            var i = v.P_LoopMain[playerID] - 4;

            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 5 + 2 * i, 64);
            trg.Shape_NxNSquare(playerID, 1, "80 + 1n Vulture", 5 + 2 * i, 64);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("80 + 1n Vulture", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 11, 64);
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Ghost", 11, 64);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 10)
         {
            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 11, 64);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 12)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 13)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {      
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);
         SetInvincibility(Disable, v.P_UnitID[playerID], playerID, "Anywhere");
         trg.ComputerAlly(0);
         
         trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, 0);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}